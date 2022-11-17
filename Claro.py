import selenium
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('C:\Github\Scraping\chromedriver.exe')
driver.get('https://www.tiendaclaro.pe/personas/catalogo-celulares/liberados')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(30)

models = driver.find_elements_by_class_name("claroperupoc-claro-general-apps-0-x-product_name_content")
prices = driver.find_elements_by_class_name("claroperupoc-claro-general-apps-0-x-product_price_container")
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