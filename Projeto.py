# Automação Web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd



navegador = webdriver.Chrome()

# Passo 01 - Pegar a cotação do Dólar

navegador.get('https://www.google.com.br/')


navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dólar")

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Cotação do Dólar:",cotacao_dolar)

# Passo 02 - Pegar a cotação do Euro

navegador.get('https://www.google.com.br/')


navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Cotação do Euro:",cotacao_euro)

# Passo 03 - Pegar a cotação do Ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')

cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print("Cotação do Ouro:",cotacao_ouro)

navegador.quit()

# Passo 04 - Importar a base de dados e Atualizar a base

tabela = pd.read_excel("Produtos.xlsx")

# Passo 05 - Recalcular os Preços

# Atualizar a cotação

# Dólar

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)

# Euro

tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)

# Ouro

tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# Recalcular os preços

# Preço de compra = cotação * preço original

# Preço de venda = preço de compra * margem

print(tabela)

# Passo 06 - Exportar a base atualizada

tabela.to_excel("Produtos Novo.xlsx",index=False)
