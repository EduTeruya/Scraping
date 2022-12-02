import Dao.sqliteDao as sqlite
import Dao.csvDao as csv

class DaoFactory:
 
    @staticmethod
    def getDao(name):
        if (name == "SQLite"):
            dao = sqlite.SqliteDao()
        else:
            dao = csv.CsvDao()
        
        return dao
        

