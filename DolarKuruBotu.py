#Have fun guys :)
#Made By dx17 and sc4

import discord
from discord.ext import commands
import requests
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

async def get_dolar_kuru():
    await bot.wait_until_ready()
    channel = bot.get_channel(UR CHANNEL ID)

    while not bot.is_closed():
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()

        if "TRY" in data["rates"]:
            dolar_kuru = data["rates"]["TRY"]
            embed = discord.Embed(title="Dolar Kuru", description=f"{dolar_kuru} TRY", color=discord.Color.green())
        else:
            embed = discord.Embed(title="Dolar Kuru", description="Dolar kuru bilgisi alınamadı.", color=discord.Color.red())

        await channel.send(embed=embed)

        await asyncio.sleep(30)

@bot.event
async def on_ready():
    print(f"We are logged in as {bot.user}")
    bot.loop.create_task(get_dolar_kuru())

bot.run("UR BOT TOKEN")
