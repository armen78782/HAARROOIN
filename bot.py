import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # Необходимо для чтения содержимого сообщений

bot = commands.Bot(command_prefix="!", intents=intents)

# Асинхронная функция для загрузки всех команд
async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != 'loader.py':  # исключаем лоадер
            try:
                bot.load_extension(f'commands.{filename[:-3]}')  # Загружаем команду (без await)
                print(f"Команда {filename} загружена.")
            except Exception as e:
                print(f"Ошибка при загрузке команды {filename}: {e}")

# Лоадер для команд
@bot.command()
async def reload(ctx):
    """Перезагружает все команды из папки 'commands'"""
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != 'reload.py':  # исключаем лоадер
            try:
                bot.reload_extension(f'commands.{filename[:-3]}')  # Перезагружаем команду (без await)
                await ctx.send(f'Команда {filename} перезагружена!')
            except Exception as e:
                await ctx.send(f'Ошибка при перезагрузке {filename}: {e}')

@bot.command()
async def привет(ctx):
    await ctx.send("Привет! Я работаю!")

# Событие, которое срабатывает при запуске бота
@bot.event
async def on_ready():
    print(f"Бот вошёл как {bot.user}")
    await load_extensions()  # Загружаем все команды при старте бота

# Запуск бота
bot.run(os.getenv("DISCORD_TOKEN"))