import selenium
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('C:\Github\Scraping\chromedriver.exe')
driver.get('https://www.tiendaclaro.pe/personas/catalogo-celulares/postpago/portabilidad/si?initialMap=c,c,c&initialQuery=personas/catalogo-celulares/postpago/portabilidad/si&map=category-1,category-2,category-3,modalidad,plan-destacado&order=&query=/personas/catalogo-celulares/postpago/portabilidad/si&searchState&utm_campaign=performance_tienda&utm_source=google&utm_medium=search&utm_content=generico-postpago_serch&utm_term=postpago-portabilidad&cu=cp1668118049&gclid=Cj0KCQiAgribBhDkARIsAASA5bumfxx1s_VzyO_me9RXf8LtNldpKXCLTkSKpEJjOjt08i4zqCU2k-EaAuAKEALw_wcB')
time.sleep(15)

models = driver.find_elements_by_class_name('claroperupoc-claro-general-apps-0-x-product_name_content')
prices = driver.find_elements_by_class_name("claroperupoc-claro-general-apps-0-x-product_price_container")


modelos = []
for model in models:
    modelos.append(model.text)

precios = []
for price in prices:
    precios.append(price.text)


# Pandas
modelos_df = pd.DataFrame({'modelos':modelos})
precios_df = pd.DataFrame({'precios':precios})

# unir los 2 frames en 1
frames = [modelos_df, precios_df]
result = pd.concat((frames), axis=1, join='inner')
print(result)



# for price in prices:
#     for model in models:
#         print((model).text, (price).text)


        