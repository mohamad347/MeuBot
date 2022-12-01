from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from decouple import config

name = config('name')
password = config('password')

# print(name)
# print(password)
chrome_options = Options()
chrome_options.headless = True 
browser = webdriver.Chrome('./chromedriver')

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