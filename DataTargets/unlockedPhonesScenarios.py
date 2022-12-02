import Dao.daoFactory as daoFac
import Pages.BitelPage as bitelPOM
import Pages.ClaroPage as claroPOM
import Pages.EntelPage as entelPOM
import Pages.MovistarPage as movistarPOM

class unlockedPhonesScenarios:

    def __init__(self):
        self.dao = daoFac.DaoFactory.getDao("SQLite")

    # def __del__(self):
    #     self.dao.close()

    def getPhonePricesFromClaro(self):
        #Get data from Page Object
        pageObject = claroPOM.claroPhoneCatalog()
        pageObject.openUrl()
        phones = pageObject.getAllItems()
        pageObject.close()
        #Saving data
        self.dao.saveData('PHONEPRICES', 'CLARO', phones, 'Modelos', 'Precios')
        return phones

    def getPhonePricesFromMovistar(self):
        #Get data from Page Object
        pageObject = movistarPOM.movistarPhoneCatalog()
        pageObject.openUrl()
        phones = pageObject.getAllItems()
        pageObject.close()
        #Saving data
        self.dao.saveData('PHONEPRICES', 'MOVISTAR', phones, 'Modelos', 'Precios')
        return phones

    def getPhonePricesFromEntel(self):
        #Get data from Page Object
        pageObject = entelPOM.entelPhoneCatalog()
        pageObject.openUrl()
        phones = pageObject.getAllItems()
        pageObject.close()
        #Saving data
        self.dao.saveData('PHONEPRICES', 'ENTEL', phones, 'Modelos', 'Precios')
        return phones

    def getPhonePricesFromBitel(self):
        #Get data from Page Object
        pageObject = bitelPOM.bitelPhoneCatalog()
        pageObject.openUrl()
        phones = pageObject.getAllItems()
        pageObject.close()
        #Saving data
        self.dao.saveData('PHONEPRICES', 'BITEL', phones, 'Modelos', 'Precios')
        return phones

    
        
