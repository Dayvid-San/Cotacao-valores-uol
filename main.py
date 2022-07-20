from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# emprese_buscada = str(input('Insira o codico da empresa que você está buscando!'))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://economia.uol.com.br/cotacoes/bolsas/'
id_inputSeach = 'filled-normal'

# O get é para ir ao site
driver.get(url)

input_busca = driver.find_element(By.ID, id_inputSeach)
# o send.keys é o comando que digita
input_busca.send_keys('PETR3.SA')

# Pelo problema de entendimeto damos um tempo para o bot apertar enter
sleep(3)
input_busca.send_keys(Keys.ENTER)
sleep(2)


span_contacao_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')

# Recebe o valor de dentro
cotacao_valor = span_contacao_val.text
print(f'A cotação da Petrobras (PETR3.SA) hoje está em {cotacao_valor}')

#input('')
