# Automação Web

# Objetivo do projeto:

# Pesquisar dados atualizados na internet, para atualizar a base de dados com valores das cotações atuais, do Dólar, Euro e Ouro.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Define o navegador "Chrome" como o navegador que será utilizado.
navegador = webdriver.Chrome()

# Passo 01 - Pegar a cotação do Dólar.

# Utiliza o link de acesso à página de pesquisa do google.
navegador.get('https://www.google.com.br/')

# Acha o elemento da barra de pesquisa, para poder utilizá-la, e escreve a sua pesquisa desejada.
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dólar")

# Acha o elemento da barra de pesquisa, para poder utilizá-la e "aperta" o ENTER, para avançar.
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Acha o elemento em que está disponível o valor atualizado do Dólar e salva-o em uma variável.
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Apenas para o controle, printa a informação no terminal.
print("Cotação do Dólar:",cotacao_dolar)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Passo 02 - Pegar a cotação do Euro

# Basicamente, repete o mesmo procedimento anterior, para o valor do Euro.

# Utiliza o link de acesso à página de pesquisa do google.
navegador.get('https://www.google.com.br/')

# Acha o elemento da barra de pesquisa, para poder utilizá-la, e escreve a sua pesquisa desejada.
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")

# Acha o elemento da barra de pesquisa, para poder utilizá-la e "aperta" o ENTER, para avançar.
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Acha o elemento em que está disponível o valor atualizado do Euro e salva-o em uma variável.
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


# Apenas para o controle, printa a informação no terminal.
print("Cotação do Euro:",cotacao_euro)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Passo 03 - Pegar a cotação do Ouro

# Um pouco diferente, mas a dinâmica é a mesma que a anterior.


# Utiliza o link para o site "Melhor Cambio" onde terá o valor do Ouro atual.
navegador.get('https://www.melhorcambio.com/ouro-hoje')

# Acha o elemento em que está disponível o valor atualizado do Ouro e salva-o em uma variável.
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')

# O valor virá desta forma: "319,39", por exemplo. E isso estará errado e não ajudará nas contas posteriomente.
# Portanto deverá ser trocada a vírgula por um ponto da seguinte forma:
cotacao_ouro = cotacao_ouro.replace(",",".")

# Apenas para o controle, printa a informação no terminal.
print("Cotação do Ouro:",cotacao_ouro)

# Fecha o navegador.
navegador.quit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Passo 04 - Importar a base de dados e Atualizar a base

# Importa a base de dados.
tabela = pd.read_excel("Produtos.xlsx")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Passo 06 - Exportar a base atualizada

# Exporta a base atualizada.
tabela.to_excel("Produtos Novo.xlsx",index=False)
