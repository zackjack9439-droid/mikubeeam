import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Miku ligada com sucesso como {bot.user}!")

@bot.command()
async def mikubeam(ctx):
    await ctx.send("MIKU MIKU BEAAAM!")

bot.run("MTUzMzU0Njc4NzQ0NzY0MDI0Nw.Gg2iD1.BsQ3Nu6obYi2W7xw69EVXo76G57Flt5BQ0sc4U")
