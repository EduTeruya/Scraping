from selenium import webdriver


class DriverFactory:
 
    @staticmethod
    def getDriver(name):
        if (name == "Chrome"):
            driver = webdriver.Chrome('./Drivers/chromedriver.exe') 
        else:
            driver = webdriver.Firefox()
        
        driver.implicitly_wait(10)
        return driver
        

