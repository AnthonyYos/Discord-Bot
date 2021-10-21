import discord
from discord.ext import commands

class LearningDiscordBot_events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Events cog loaded")
    

    # Called when messages are sent
    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.bot.user:
            return

        # Banned words list
        # .strip() gets rid of new lines
        banned_words = [line.lower().strip() for line in open("badwords.txt","r")]

        # Delete messages containing banned words
        if any(word in message.content for word in banned_words):
            await message.delete()
            await message.channel.send("Please don't say that here")
        
        if "hello" in message.content.lower():
            await message.channel.send(f"Hi")

        if self.bot.user.mentioned_in(message):
            await message.channel.send("Don't @ me please")


    # Send message to new users, joining the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} has joined the server")
        await member.send(f"Hi {member.name}, welcome to {member.guild.name}.")
        # await member.create_dm()
        # await member.dm_channel.send(f"Hi {member.name}, welcome to the discord")
    
    # Prints a message of when a user leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member.name} has left the server")

    # Bot posts error handling messages for commands in various situations
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # User input
        if isinstance(error, discord.ext.commands.UserInputError):
            await ctx.send(f"Used the wrong inputs for the '!{ctx.command.name}' command.\nType '!help {ctx.command.name}' to see the correct inputs.")
            return

        # Missing inputs
        if isinstance(error, discord.ext.commands.MissingRequiredArgument):
            await ctx.send(f"Missing input(s) for the '!{ctx.command.name}' command.\nType '!help {ctx.command.name}' to see the inputs needed.")
            return
        
        # Unknown command
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await ctx.send("Unknown command, double check you're spelling.\nType '!help' to get a list of commands.")
            return

        # Missing permissions
        if isinstance(error, discord.ext.commands.MissingPermissions):
            await ctx.send(error)
            return


def setup(bot):
    bot.add_cog(LearningDiscordBot_events(bot))