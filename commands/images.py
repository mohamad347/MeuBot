from discord.ext import commands
import discord


class Images(commands.Cog):
    '''Works with images(embed)'''

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'foto',help='embed')
    async def get_random_image(self,ctx):
        url_image = 'https://picsum.photos/1920/1080'

        embed_image = discord.Embed(
            title = 'Resultado da busca da imagem',
            description = 'A imagem é totalmente aleatória',
            color = 0x0000FF, #cor ta em hexadecimal, no caso esse é o azul
        )

        embed_image.set_author(name= self.bot.user.name,icon_url= self.bot.user.avatar_url)
        embed_image.set_footer(text='Feito por ' + self.bot.user.name,icon_url=self.bot.user.avatar_url)

        embed_image.add_field(name="API",value="usamos a API do https://picsum.photos")
        embed_image.add_field(name="Parâmetros",value= '{largura}/{altura}')
        embed_image.add_field(name='Exemplo',value=url_image,inline=False) #o inline ja vem como true. Quando vc coloca como false, o field novo ocupa todo o espaço

        embed_image.set_image(url=url_image)

        await ctx.send(embed= embed_image)
        
def setup(bot):
    bot.add_cog(Images(bot))