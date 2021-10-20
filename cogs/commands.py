import random
from discord.ext import commands

class LearningDiscordBot_commands(commands.Cog, name = "User Commands"):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands cog loaded")


    # Roll Dice command
    @commands.command(help = "Rolls x-amount of y-sided dice.")
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        try:
            if number_of_dice <= 0 or number_of_sides <= 0:
                raise ValueError
            # if isinstance(number_of_dice,int) != True or isinstance(number_of_sides,int) != True:
            #     raise TypeError
        # REMINDER this works because of list comprehension
            dice = [
                str(random.randint(1, number_of_sides))
                for dice in range(number_of_dice)
            ]
        except (ValueError):
            await ctx.send("Input value(s) must be an integer value of 1 or greater.")
        # except (TypeError):
        #     await ctx.send("Input value(s) must be a/an integer(s)")
            
        await ctx.send(", ".join(dice))

    # 8ball command
    @commands.command(name = "8ball", help='Responds with a random 8-ball saying.')
    async def magic_8_ball(self, ctx):
        magic_8_ball_quotes = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it."
        ]

        response = random.choice(magic_8_ball_quotes)
        await ctx.send(response)
    

    @commands.command(help='Coin flip responds w/ head or tail.')
    async def coin(self, ctx):
        coin = ["Heads","Tails"]
        response = random.choice(coin)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(LearningDiscordBot_commands(bot))