from discord.ext import commands
import discord

class Talks(commands.Cog):
    '''Talks with user'''

    def __init__(self,bot):
        self.bot = bot

    # bot.command -> commands.command
    @commands.command(name = "oi",help='Manda um oi(não requer argumentos)')
    async def send_hello(self,ctx): #quando mandar !oi, o bot responde Olá, 'nome'
        name = ctx.author.name

        response = "Eaeeeee, " + name

        await ctx.send(response)

    @commands.command(name='segredo',help='manda uma mensagem no privado')
    async def secret(self,ctx): #mandar mensagem no privado
        try:
            await ctx.author.send('Hello')
            await ctx.author.send('Moha aqui!')
        
        except discord.errors.Forbidden:
            await ctx.send('Não posso te mandar mensagem, habilite receber mensagens de qualquer pessoa no privado(configurações>privacidade)')

def setup(bot):
    bot.add_cog(Talks(bot))