import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # Необходимо для чтения содержимого сообщений

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот вошёл как {bot.user}")

# Лоадер для команд
@bot.event
async def on_ready():
    print(f"Бот вошёл как {bot.user}")
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[:-3]}')

@bot.command()
async def привет(ctx):
    await ctx.send("Привет! Я работаю!")

# Запуск бота
bot.run(os.getenv("DISCORD_TOKEN"))
