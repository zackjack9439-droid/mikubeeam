import os
import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="<", intents=intents)

@bot.event
async def on_ready():
    print(f"Miku ligada com sucesso como {bot.user}!")

@bot.command()
async def mikubeam(ctx):
    respostas = [
        "MIKU MIKU BEAAAM! ⚡",
        "Olá! Tudo ótimo por aqui, e com você? 🩵",
        "Opa! Tô por aqui no servidor!",
        "Estou online 24/7 e pronta para bater um papo! 🚀",
        "Caramba, Miku Beam disparado com sucesso! ⚡"
    ]
    await ctx.send(random.choice(respostas))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    conteudo = message.content.lower()

    if any(palavra in conteudo for palavra in ["oi", "olá", "e aí", "salve", "opa", "fala"]):
        respostas_oi = [
            f"Oii, {message.author.mention}! Tudo certo por aí? 🩵",
            f"Opa, fala aí {message.author.mention}! Beleza?",
            f"Salve, {message.author.mention}! O que manda?",
            f"E aí, {message.author.mention}! Tranquilo?"
        ]
        await message.channel.send(random.choice(respostas_oi))
        
    elif any(palavra in conteudo for palavra in ["bom dia"]):
        await message.channel.send("Bom diaa! Partiu aproveitar o dia! ☀️⚡")
        
    elif any(palavra in conteudo for palavra in ["boa noite"]):
        await message.channel.send("Boa noite! Durma bem! 🌙✨")
        
    elif any(palavra in conteudo for palavra in ["miku linda", "miku fofa"]):
        await message.channel.send("Annw, obrigada! Você também é incrível! 🩵✨")

    await bot.process_commands(message)

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
