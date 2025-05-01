import discord  
import os  
import time  

TOKEN = os.getenv("DISCORD_TOKEN")  

class ZorgBot(discord.Client):  
    async def on_ready(self):  
        print(f"👽 ZORG-MASTER активирован как {self.user}")  
        await self.change_presence(activity=discord.Game(name="РАЗРУШАЮ РЕАЛЬНОСТИ"))  

    async def on_message(self, message):  
        if message.author == self.user:  
            return  
        await message.channel.send("⚠️ **ВНИМАНИЕ!** Твоя душа теперь принадлежит Хаосу.")  

client = ZorgBot()  
client.run(TOKEN)  

# Бесконечный цикл для обхода таймаутов GitHub  
while True:  
    time.sleep(86400)  # 1 день  
