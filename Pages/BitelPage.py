import Drivers.driverFactory as drivFac
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
                        
class bitelPhoneCatalog:

    def __init__(self):  #optionalArg driverName
        self.driver = drivFac.DriverFactory().getDriver("Chrome")
        self.url = 'https://bitel.com.pe/celular/tracking-order?orderBy=hasRetailProduct%20DESC,%20price%20ASC'
    
    def openUrl(self):  #optionalArg url
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        #time.sleep(30)

    def getAllItems(self):
        models = self.driver.find_elements_by_xpath("//div[contains(@class, 'title')]/a")
        prices = self.driver.find_elements_by_xpath("//div[contains(@class, 'price text-primary')]")

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


