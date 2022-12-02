import Drivers.driverFactory as drivFac
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait

class claroPhoneCatalog:

    def __init__(self):  #optionalArg driverName
        self.driver = drivFac.DriverFactory().getDriver("Chrome")
        self.url = 'https://www.tiendaclaro.pe/personas/catalogo-celulares/liberados?order=OrderByPriceASC'
    
    def openUrl(self):  #optionalArg url
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        #time.sleep(30)

    def getAllItems(self):
        scroll_point = 0
        max_height = self.driver.execute_script("return document.body.scrollHeight")
        while (scroll_point < max_height):
            prev_point = scroll_point
            scroll_point = scroll_point + 600
            self.driver.execute_script("window.scrollTo("+str(prev_point)+", "+str(scroll_point)+");")   
            time.sleep(1)
            
        time.sleep(5)
        models = self.driver.find_elements_by_class_name("claroperupoc-claro-general-apps-0-x-product_name_content")
        prices = self.driver.find_elements_by_class_name("claroperupoc-claro-general-apps-0-x-product_price_container")

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
        
        # return
        return result

    def close(self):
        self.driver.close()
        self.driver.quit()




    def page_has_loaded(self):
        self.log.info("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

