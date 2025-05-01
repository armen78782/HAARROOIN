async def reload(ctx):
    """Перезагружает все команды из папки 'commands'"""
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != 'reload.py':  # исключаем лоадер
            try:
                bot.reload_extension(f'commands.{filename[:-3]}')  # Перезагружаем команду
                await ctx.send(f'Команда {filename} перезагружена!')
            except Exception as e:
                await ctx.send(f'Ошибка при перезагрузке {filename}: {e}')
