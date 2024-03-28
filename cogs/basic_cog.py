import discord
from discord.ext import commands
import pickledb
class Basic(commands.Cog, name="Basic"):
    def __init__(self, bot):
      
        self.bot = bot
        self.db = pickledb.load("data.db", True)

  
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content == "!current":
            return
        
        if not self.db.get(str(message.author.id)):
            print('hey')
            self.db.set(str(message.author.id), "1")
        

        self.db.set(str(message.author.id), str(int(self.db.get(str(message.author.id)))+1))

    @commands.command()
    async def current(self, ctx):
        current = self.db.get(str(ctx.author.id))
        await ctx.send(current)
        

async def setup(bot):
    await bot.add_cog(Basic(bot))
        