import discord
from dotenv import load_dotenv
import os

from discord.ext import commands
from Util.player import Player
class Basic(commands.Cog, name="Basic"):
    def __init__(self, bot):
        load_dotenv()
        self.BASE_URL = os.getenv('BASE_URL')
        self.bot = bot
        self.player = Player()

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await self.player.createPlayer(member.id)

    @commands.command()
    async def sendMoney(self, ctx, amount: float, member: discord.Member):
        if amount < 0:
            await ctx.send("no way you really trying that loser")
            return
        if member.id == ctx.author.id:
            await ctx.send("bruh tryna send money to himself BAHAHA")
            return
        
        senderExists = await self.player.exists(ctx.author.id)
        recipientExists = await self.player.exists(member.id)
        if not senderExists or not recipientExists or member.id == 1222596523313991732:
            await ctx.send("someone aint a player dawg")
            return
       
        
        
        res = await self.player.sendMoney(ctx.author.id, member.id, amount)
        if not res:
            await ctx.send("dawg  you aint got enough money LLMFAO")
            return
       
        await ctx.send("sent $" + str(amount) + " to " + "<@" + str(member.id) + ">")
        

    @commands.command()
    async def myMoney(self, ctx):
        player = await self.player.MONEY(ctx.author.id)
        if not player:
            await ctx.send("You are not a registered user!")
            return
        
        await ctx.send("You have $" + str(player) + " USD.")
        
        

async def setup(bot):
    await bot.add_cog(Basic(bot))
        