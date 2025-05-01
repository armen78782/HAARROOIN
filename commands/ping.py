import discord
from discord.ext import commands
import time

@commands.command()
async def ping(ctx):
    """Команда для проверки пинга"""
    start_time = time.time()  # Засекаем время до ответа
    message = await ctx.send("Пингуем...")  # Отправляем сообщение
    end_time = time.time()  # Засекаем время после получения ответа
    ping_time = (end_time - start_time) * 1000  # Время в миллисекундах
    await message.edit(content=f"Понг! Пинг: {ping_time:.2f}ms")  # Изменяем сообщение с пингом
