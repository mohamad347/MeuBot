from discord.ext import commands, tasks
import discord
import datetime


class Dates(commands.Cog):
    '''Works with dates'''

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       self.current_time.start()

    @tasks.loop(hours = 1)
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y as %H:%M:%S")

        channel = self.bot.get_channel(1005182775835496571) #dentro fica o id do canal

        await channel.send("Data atual: " + now)


def setup(bot):
        bot.add_cog(Dates(bot))