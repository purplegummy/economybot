import discord
from dotenv import load_dotenv
from discord.ext import commands
from Util.player import Player
import os
import requests
import json
import requests
from datetime import datetime, time

class Stocks(commands.Cog, name="Stocks"):
    def __init__(self, bot):
        self.bot = bot
        self.player = Player()

        load_dotenv()
        TOKEN = os.getenv('ALPHA_TOKEN')
        self.stocks_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=' + TOKEN
            

 
    
    @commands.command()
    async def buyStock(self, ctx, name: str, shares: int):
        # should say not 

        if self.stockMarketAvailable():
            await ctx.send("Unavailable!")

        price = float(self.getStockPrice(name))
        playerMoney= await self.player.MONEY(ctx.author.id)
        print(playerMoney)
        if not self.canBuy(price, shares, playerMoney):
            await ctx.send("Not able to purchase...Maybe you don't have enough money?")
            return
        


        await ctx.send("bought that shi cuzzo! for about " + str(round(price*shares, 2)) +  " dollars dawg")
        
        #need to keep track of what stocks they have money in
            
        

    @commands.command()
    async def sellStock(self, ctx, name: str):
        pass
 
    def getStockPrice(self, name: str):
        data = requests.get(self.stocks_url.replace("IBM", name)).json()
        if not data:
            return None
        return data["Global Quote"]["05. price"]
    
    def canBuy(self, price, shares, playerMoney):
        if playerMoney - price*shares < 0: 
            return False
        return True  # check if it is  over market volume too
    
    def stockMarketAvailable(self) -> bool:
        dt = datetime.now()
        if dt.weekday() >=5:
            return False
        
        start = time(9,30)
        end = time(16)
        now = dt.time()
        
        if start <= end:
            return start <= now < end
        else:
            return start <= now or now < end
        
     
        

async def setup(bot):
    await bot.add_cog(Stocks(bot))
        