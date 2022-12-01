import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.instagram.com/sasel.usp/')
content = BeautifulSoup(response.text,'html.parser')

#div class="_aa_y _aa_z _aa_-">
#<div class="x1n2onr6 xeuugli xs83m0k x1q0g3np x78zum5 x6s0dn4">
#<div class="_aacl _aacp _aacu _aacx _aad6 _aade"><span class="_ac2a">437</span>
#class="x9f619 x1n2onr6 x1ja2u2z"
conteudo = content.find('div',attrs={'id':'mount_0_0_K6'})
#print(content.prettify())
print(response)