import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos_df = pd.read_excel("Enviar2.xlsx")
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) <1:
    time.sleep(1)

for i, mensagem in enumerate (contatos_df['Mensagem']):
    nome = contatos_df.loc[i, "Nome"]
    celular = contatos_df.loc[i, "Celular"]
    texto = urllib.parse.quote(f"Olá {nome}! Seu login e senha do SEI: {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={celular}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) <1:
         time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
    time.sleep(10)

         


        
         
         



