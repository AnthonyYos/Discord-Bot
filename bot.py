# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv("TOKEN.env")

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents = intents)

# Needed to load cogs if admin cog is unloaded
@bot.command(hidden = True, help = "Use to load cogs to discord bot\n<extension> = filename, do not put file extension")
@commands.has_permissions(administrator=True)
async def load(ctx,extension):
    try:
        bot.load_extension(f"cogs.{extension}")
        print(f"cogs.{extension} has been loaded")
    except Exception:
        await ctx.send("Could not load cog")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(os.getenv('DISCORD_TOKEN'))