from discord.ext import commands

# @commands.has_permissions(administrator=True) this hides commands from users not marked as admins
class Admin(commands.Cog, name = "Admin-Only Commands"):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands cog loaded")


    # Unload cog
    @commands.command(help = "Use to unload cogs from discord bot\n<extension> = filename.")
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f"cogs.{extension}")
            print(f"cogs.{extension} has been unloaded.")
        except Exception:
            print(f"cogs.{extension} could not be unloaded.")

    # Reload cog
    @commands.command(help = "Use to unload and reload cogs\nWill not work if cog isn't already loaded.")
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        try:
            self.bot.reload_extension(f"cogs.{extension}")
            print(f"cogs.{extension} has been reloaded.")
        except Exception:
                print(f"cogs.{extension} could not be reloaded.")


    # Purge chat
    @commands.command(help="Clears x-amount of messages, command prompt is included in the count.")
    @commands.has_permissions(administrator=True)
    async def clear(self,ctx, number_of_messages: int):
        await ctx.channel.purge(limit = number_of_messages+1)

    # Add to banned words list
    @commands.command(name ="ban_word", help = "Adds a new word to the list of banned words")
    @commands.has_permissions(administrator=True)
    async def add_word(self, ctx, word: str):
        # Load words into set
        with open("badwords.txt","r") as f:
            banned_words = {line.lower().strip() for line in f}
        f.close()
        # Check if word is already banned
        if word not in banned_words:
            with open("badwords.txt","a") as f:
                await ctx.send(f"This is now a bad word")
                await f.writelines("\n" + word.lower())
            f.close()
        else:
            await ctx.send(f"That is already a bad word")

def setup(bot):
    bot.add_cog(Admin(bot))