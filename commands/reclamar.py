from codecs import namereplace_errors
from unicodedata import name
from discord.ext import commands
import discord

class Reclamar(commands.Cog):
    '''para reclamar de algum comando'''
    
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='reclamar',help='Use esse comando para reclamar de um comando defeituoso(argumento: nome do canal que quer mandar')
    async def reclame(self,ctx,channel_name,command,*message):
        #channel = client.get_channel(channel_id)
        commands = [c.name for c in self.bot.commands]

        channel = discord.utils.get(ctx.guild.channels,name=channel_name) #dá certo usando o nome
        #channel = self.bot.get_channel(1009213171984252960)  #da certo mas só consigo acessar pelo id
        for x in commands:
            if x==command:

                message = ' '.join(message)
                #messages = []
                #messages.append(message)
                await channel.send(message)
            
           


def setup(bot):
    bot.add_cog(Reclamar(bot))
