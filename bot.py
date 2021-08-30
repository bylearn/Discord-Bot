import os
from decouple import config
from discord.ext import commands

bot = commands.Bot("!")


def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("tasks.dates")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")


load_cogs(bot)

TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)
