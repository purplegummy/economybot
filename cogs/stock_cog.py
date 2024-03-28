import discord
from dotenv import load_dotenv
from discord.ext import commands

import os
import requests
import json
import requests
from datetime import datetime, time
class Stocks(commands.Cog, name="Stocks"):
    def __init__(self, bot):
        self.bot = bot
      
        load_dotenv()
        TOKEN = os.getenv('ALPHA_TOKEN')
        self.url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=' + TOKEN
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        
        user = requests.post("http://127.0.0.1:8000/addMember/",data=json.dumps({"memberId": member.id, "money": 2000}) )
        print(str(user.content))
            

 
    
    @commands.command()
    async def buyStock(self, ctx, name: str, shares: int):
        # should say not 
        if self.stockMarketAvailable():
            await ctx.send("Unavailable!")

        price = int(self.getStockPrice(name))
        playerMoney= self.playerMoney(str(ctx.author.id))

        if not self.canBuy(price, shares, playerMoney):
            await ctx.send("Not able to purchase...Maybe you don't have enough money?")
        

        
        #need to keep track of what stocks they have money in
            
        

    @commands.command()
    async def sellStock(self, ctx,name):
        pass
 
    def getStockPrice(self, name):
        data = requests.get(self.url.replace("IBM", name)).json()
        if not data:
            return None
        return data["Global Quote"]["05. price"]
    def canBuy(self, price, shares, playerMoney):
        if playerMoney - price*shares < 0: 
            return False
        return True  # check if it is  over market volume too
    def playerMoney(self, memberId):
        money = json.loads(self.db.get(memberId))["money"]
        return int(self.db.get(memberId))
    
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
        
     
    
   
    

    @commands.command()
    async def currentStanding(self, ctx):
        current = self.db.get(str(ctx.author.id))
        await ctx.send(current)
        

async def setup(bot):
    await bot.add_cog(Stocks(bot))
        