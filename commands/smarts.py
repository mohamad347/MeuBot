from discord.ext import commands


class Smart(commands.Cog):
    '''Solves dumb calculations for dumb people'''

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name= "calcular",help='calcula expresssao(argumento necessario: expressao matematica') #função para calcular uma expressao matematica
    async def calculate_expression(self,ctx,*expression): #esse * é pra quando vc n sabe o numero de argumentos e ele interpreta como um só(agr expression é um tupple)
        expression = ''.join(expression)
        response = eval(expression) #funçao perigosa. Desse jeito, a funçao ignora o espaço, entao se colocar 1 + 1, o discord n reconhece

        await ctx.send("A resposta é: " + str(response))


def setup(bot):
    bot.add_cog(Smart(bot))