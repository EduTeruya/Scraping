import selenium
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('C:\Github\Scraping\chromedriver.exe')
driver.get('https://tienda.movistar.com.pe/celulares/liberados')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(30)

models = driver.find_elements_by_class_name("product-item-link hv-equipo-nombre product-item-name w-100 d-block Liberados   f-f-Telefonica-Light class_name_redirect")
prices = driver.find_elements_by_class_name("itemDetail-value-3 color-azulDetail f-f-Telefonica-Light")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(30)

modelos = []
for model in models:
    modelos.append(model.text)

precios = []
for price in prices:
    precios.append(price.text)


# Pandas
modelos_df = pd.DataFrame({'Modelos':modelos})
precios_df = pd.DataFrame({'Precios':precios})

# unir los 2 frames en 1
frames = [modelos_df, precios_df]
result = pd.concat((frames), axis=1, join='inner')
print(result)

#arreglar la columna de precios aparece una fila mas abajo

