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
        if message.author == self.bot.user:
            return
        
        if "hello" in message.content.lower():
            await message.channel.send(f"Hi")

        if self.bot.user.mentioned_in(message):
            await message.channel.send("Don't @ me please")


    # Send message to new users, joining the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"Hi {member.name}, welcome to {member.guild.name}")
        # await member.create_dm()
        # await member.dm_channel.send(f"Hi {member.name}, welcome to the discord")
    




def setup(bot):
    bot.add_cog(LearningDiscordBot_events(bot))