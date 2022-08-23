from discord.ext import commands
'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options'''
from decouple import config
import requests
from bs4 import BeautifulSoup


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

    '''@commands.command(name='clima',help = 'comando para clima de hoje')
    async def climate():
        chrome_options = Options()
        chrome_options.headless = True 
        navegador = webdriver.Chrome(options=chrome_options)
        navegador.get('https://www.google.com.br/')'''

    @commands.command(name='clima',help='Descreve o clima de hoje e fala a temperatura(argumento:cidade)')
    async def climate(self,ctx,city):
        API_KEY = config('API_KEY')
        #city = input('digite a cidade: ')
        link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br' #isso lá em api do site
        request = requests.get(link)
        #print(request) # se for 200 -> funcionou, 404 -> nao encontrado, 500 -> servidor nao disponivel
        #print(request.json())
        request_dict = request.json()
        description = request_dict['weather'][0]['description']
        temp = request_dict['main']['temp'] - 273
        await ctx.send(f'Descrição: {description}\nTemperatura: {temp:.2f}')

    @commands.command(name='noticia',help='Trazendo as noticias pra vc')
    async def news(self,ctx):
        #topics = ' '.join(topic)
        response = requests.get('https://g1.globo.com/')

        content = response.content

        site = BeautifulSoup(content,'html.parser')

        posts = site.findAll('div',attrs={'class':'feed-post-body'})
        
        for noticia in posts:
            title = noticia.find('a',attrs={'class':'feed-post-link'})
            time = noticia.find('span',attrs={'class':'feed-post-datetime'})

            subheader = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

            if subheader:
                await ctx.send(f'{title.text}\n{subheader.text}\n{time.text}\n{title["href"]}\n')

            else:
                await ctx.send(f'{title.text}\n{time.text}\n{title["href"]}\n')

    @commands.command(name='fofoca',help='Trazendo as melhores fofocas pra vc(não tem argumentos)')
    async def breaking_news(self,ctx):
        site = requests.get('https://hugogloss.uol.com.br/famosos/')

        content = BeautifulSoup(site.text,'html.parser')

        fofocas = content.findAll('div',attrs={'class':'featured-post category-famosos'})

        for fofoca in fofocas:
            title = fofoca.find('h2',attrs={'class':'featured-title'} )
            link = fofoca.find('a',attrs={'class':'featured-content'} )
            image = fofoca.find('img',attrs={'class':'image-thumb'})

            await ctx.send('Manchete: ' + title.text)
            await ctx.send('Imagem: ' + image['src'])
            await ctx.send('Link: ' + link['href']+'\n')


def setup(bot):
    bot.add_cog(Crypto(bot))