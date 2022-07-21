from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import json

# emprese_buscada = str(input('Insira o codico da empresa que você está buscando!'))
# 
companys = ['PETR3.SA', 'MGLU3.SA', 'VIVT3']
valores = list()
data_hora = list()

def buscandoValores(company):

    id_inputSeach = 'filled-normal'
    input_busca = driver.find_element(By.ID, id_inputSeach)
    # o send.keys é o comando que digita
    input_busca.send_keys(company)

    # Pelo problema de entendimeto damos um tempo para o bot apertar enter
    sleep(2)
    input_busca.send_keys(Keys.ENTER)
    sleep(1)

    span_cotacao_titulo = driver.find_element(By.XPATH, '//span[@class="chart-info-text"]')
    span_contacao_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')

    # Recebe o valor de dentro
    cotacao_titulo = span_cotacao_titulo.text
    cotacao_valor = span_contacao_val.text

    valores.append(cotacao_valor)
    data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    print(f'{cotacao_titulo} da empresa com o codigo {company} hoje está em {cotacao_valor} às {data_hora}')


    i = 0
    while (i < len(company)):
        i = 1 + i
        input_busca.send_keys(Keys.BACK_SPACE)

    sleep(1)
        



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://economia.uol.com.br/cotacoes/bolsas/'


# O get é para ir ao site
driver.get(url)


for company in companys:
    buscandoValores(company)
    cotacao_dia = '{\n    "cotacao": [\n        {\n            "empresa": "{}",\n            "Valor": "{}",\n            "Data": "{}"\n        \n}    \n]}'.format(cotacao_valor)




driver.close()


with open(r'.\cotacao.json', 'w') as json_file:
    json.dumps(cotacao_dia, json_file, indent=4)