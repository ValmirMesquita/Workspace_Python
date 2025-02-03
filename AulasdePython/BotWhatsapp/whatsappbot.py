# Sistema para envio de mensagem altomatica no whatsapp
# importe das bibliotecas

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navega ate o Whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

# Definir contatos e grupos e mensagens a ser enviados
contatos = ['+55 98 9211-8178']
mensagem = 'Ola bom dia a todos , Paz e bem'

# Campo pesquisa 'copyable-text selectable-text'
def buscar_contato(contatos):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class="copyable-text selectable-text")]') 
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
      
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    



