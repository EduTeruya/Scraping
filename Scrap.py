import time

import selenium
from selenium import webdriver

driver = webdriver.Chrome('C:\Github\Scraping\chromedriver.exe')
driver.get('https://www.tiendaclaro.pe/personas/catalogo-celulares/postpago/portabilidad/si?initialMap=c,c,c&initialQuery=personas/catalogo-celulares/postpago/portabilidad/si&map=category-1,category-2,category-3,modalidad,plan-destacado&order=&query=/personas/catalogo-celulares/postpago/portabilidad/si&searchState&utm_campaign=performance_tienda&utm_source=google&utm_medium=search&utm_content=generico-postpago_serch&utm_term=postpago-portabilidad&cu=cp1668118049&gclid=Cj0KCQiAgribBhDkARIsAASA5bumfxx1s_VzyO_me9RXf8LtNldpKXCLTkSKpEJjOjt08i4zqCU2k-EaAuAKEALw_wcB')
time.sleep(10)

models = driver.find_elements_by_class_name('claroperupoc-claro-general-apps-0-x-product_name_content')
prices = driver.find_elements_by_class_name('claroperupoc-claro-general-apps-0-x-product_price_value')



for price in prices:
    print((price).text)

for model in models:
    print((model).text)

'''for price in prices:
    for model in models:
        print((model, price).text)
'''