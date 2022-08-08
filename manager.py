from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound,MissingRequiredArgument


class Manager(commands.Cog):
    '''Manage the bot'''

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): #executa quando bot estiver pronto
        print(f"Estou pronto! Estou conectado como {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self,message): #ve as mensagens e faz oq mandar
        if message.author == self.bot.user:
            return

        if "bom dia" in message.content:
            await message.channel.send(f"VAI DORMIR, {message.author.name}!") 
            await message.delete()

        #await self.bot.process_commands(message)  não precisa mais aqui, se não ele manda 2x

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite !help para ver os parâmetro necessários de cada comando")
        elif isinstance(error,CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver os comandos disponíveis")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))