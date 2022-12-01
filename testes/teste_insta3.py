from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


browser = webdriver.Chrome('./chromedriver')

browser.get('https://instagram.com')

username = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username.send_keys('hello34789')
password.send_keys('Teste1')

submit = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']")))
submit.click()

remember = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')))
remember.click()

notifications = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
notifications.click()

browser.get('https://instagram.com/sasel.usp')
time.sleep(2)
#WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div'))).click()

#posts = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/div/span'))).text
#print(posts)
#ha 7 minutos
WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div/div/div/div[1]/a/div'))).click()
#/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]
#texto = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]'))).text
last_post_time = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/div/div/a/div/time'))).text
print(last_post_time)
print(last_post_time[-1:-8])
print(int(last_post_time[3:5]))
if 'MINUTOS' in last_post_time:
    print('Nova publicação, vá la curtir')
elif 'HORAS' in last_post_time:
    if int(last_post_time[3:5])<3:
        print('Nova publicação, va la curtir')

stop = 0
last_posts_count = 0
'''while stop == 0:
    browser.get('https://instagram.com/hello34789')
    posts = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/div/span'))).text
    if last_posts_count>0:
        print(f'Voce tinha {last_posts_count} publicacoes')
    posts = int(posts)
    print(f'Agora voce tem {posts} publicacoes')
    if (posts>last_posts_count) and (last_posts_count>0):
        print('Nova publicação')
    last_posts_count = posts
    time.sleep(10)'''
