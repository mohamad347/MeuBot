from discord.ext import commands, tasks
import discord
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from decouple import config

class Dates(commands.Cog):
    '''Works with dates'''

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       self.current_time.start()
       self.new_post.start()

    @tasks.loop(hours = 1)
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y as %H:%M:%S")

        channel = self.bot.get_channel(1005182775835496571) #dentro fica o id do canal

        await channel.send("Data atual: " + now)

    @tasks.loop(hours=2,minutes=10)
    async def new_post(self):
        channel = self.bot.get_channel(1005182775835496571)

        name = config('name')
        password = config('password')
        chrome_options = Options()
        chrome_options.headless = True 
        browser = webdriver.Chrome('./chromedriver',options=chrome_options)

        browser.get('https://instagram.com')

        time.sleep(3)
        browser.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').click()
        browser.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(name)

        browser.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').click()
        browser.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)

        browser.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
        time.sleep(3)

        browser.get('https://instagram.com/hello34789')
        time.sleep(2)

        browser.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div/div/div/div[1]/a/div').click()
        time.sleep(2)

        last_post_time = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/div/div/a/div/time'))).text
        post = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span'))).text
        tag = post[post.index('['):post.index(']')+1]
        print(last_post_time)
        print(f'Saiu post novo de {tag}!!\n' + 'Vai lá curtir!\n' + 'https://instagram.com/hello34789')
        #print(last_post_time)

        if 'SEGUNDOS' in last_post_time:
            await channel.send(f'Saiu post novo de {tag}!!\n' + 'Vai lá curtir!\n' + 'https://instagram.com/hello34789')
        if 'MINUTOS' in last_post_time:
            await channel.send(f'Saiu post novo de {tag}!!\n' + 'Vai lá curtir!\n' + 'https://instagram.com/hello34789')
        elif 'HORAS' in last_post_time:
            if int(last_post_time[3:5])<3:
                await channel.send(f'Saiu post novo de {tag}!!\n' + 'Vai lá curtir!\n' + 'https://instagram.com/hello34789')
        else:
            await channel.send('Sem novas publicacoes')


def setup(bot):
        bot.add_cog(Dates(bot))