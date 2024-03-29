import discord
from dotenv import load_dotenv
import os

from discord.ext import commands
from Util.player import Player
class Lottery(commands.Cog, name="Lottery"):
    def __init__(self, bot):
        load_dotenv()
        self.BASE_URL = os.getenv('BASE_URL')
        self.bot = bot
        self.player = Player()
        self.lotteryTypes = ['Butt Ticket', 'Less Butt Ticket', 'Okay Ticket','Can You Even Afford This Ticket']
        self.lotteryPrices = [5.00, 10.00, 20.00, 100.000]
        self.lotteryMaxWinProbabilities = [.0003, 0.0003, 0.0003, 0.000002]
        self.lotteryMaxReward = [3000.0, 5000.0, 10000.0, 100000.0]
        self.lotteryOptions = {
            'Butt Ticket': {
                'price': 5.00,
                'maxWinProbability': .0003,
                'midWinProbability': .02,
                'minWinProbability': .01,
            },
            'Less Butt Ticket': {
                'price': 10.00,
                'maxWinProbability': 0.0003,
                'midWinProbability': 0.002,
                'minWinProbability': 0.001,
            },
            'Okay Ticket': {
                'price': 20.00,
                'maxWinProbability':  0.0003,
                'midWinProbability': 0.0002,
                'minWinProbability': 0.0001,
            },
              'Okay Ticket': {
                'price': 100.00,
                'maxWinProbability': 0.000002,
                'midWinProbability': .00002,
                'minWinProbability': 0.0003,
            },

        }
 
        
        

async def setup(bot):
    await bot.add_cog(Lottery(bot))
        