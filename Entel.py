import selenium
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('C:\Github\Scraping\chromedriver.exe')
driver.get('https://miportal.entel.pe/personas/catalogo/liberados')

time.sleep(15)

# no me sale esta parte
models = driver.find_elements_by_class_name('enew-sku-name p-name')
prices = driver.find_elements_by_class_name('entel-thumbnail-phone-card-new-detail__phone-initialfee offer-price')



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