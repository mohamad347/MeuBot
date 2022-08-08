from discord.ext import commands
import requests

class Crypto(commands.Cog):
    '''Works with cryptos'''

    def __init__(self,bot):
        self.bot = bot

    @commands.command(help='converte diferentes moedas(argumentos: moeda,base)')
    async def binance(self,ctx,coin,base):
        try:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')

            data = response.json() #no site, a resposta ta em json:  symbol	:"BNBBTC" price	:"0.01363700"
            price = data.get('price')

            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"o par {coin}/{base} é inválido")

        except Exception as error: #armazena o erro na variavel error
            await ctx.send('OPS... deu pau')
            print(error)

def setup(bot):
    bot.add_cog(Crypto(bot))