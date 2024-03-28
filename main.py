from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
def main(): 
  
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)


    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
    bot.run(TOKEN)
        


    

if __name__ == "__main__":
    main()