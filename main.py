import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="<", intents=intents)

@bot.event
async def on_ready():
    print(f"Miku ligada com sucesso como {bot.user}!")

@bot.command()
async def mikubeam(ctx):
 await ctx.send("MIKU MIKU BEAAAM!")

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
