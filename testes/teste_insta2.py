from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


'''chrome_options = Options()
chrome_options.headless = True 
navegador = webdriver.Chrome(options=chrome_options)'''

navegador = webdriver.Chrome()


navegador.get('https://www.instagram.com')
navegador.find_element('xpath','//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('hello34789')

#followers = navegador.find_element('xpath','//*[@id="mount_0_0_p2"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/button/div/span').get_attribute('title')
#followers = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mount_0_0_p2"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/button/div/span')))
#print(followers)

#navegador.get('https://www.google.com.br/')
# pesquisar cotaçao dolar no google
# .send_keys para escrever, .click para clicar, .get para pegar um elemento

'''navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)'''


