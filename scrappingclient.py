import  sqlite3
import DataTargets.unlockedPhonesScenarios as unlockPhones
import pandas as pd
import time

# (1) DEJO VACIA LA TABLA
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''DELETE from PHONEPRICES''')
conn.commit()
conn.close()


# (2) EJECUTO SCRAPPING PARA EL TARGET Y FUENTES QUE DESEO
 
# (2.1) Defino un target: Precios de celulares
target = unlockPhones.unlockedPhonesScenarios()

###     Fuente 1 - BITEL
print("Scrapping BITEL...")
result = target.getPhonePricesFromBitel()
time.sleep(10)

###     Fuente 2 - CLARO
print("Scrapping CLARO...")
result = target.getPhonePricesFromClaro()
time.sleep(10)

###     Fuente 3 - ENTEL
print("Scrapping ENTEL...")
result = target.getPhonePricesFromEntel()
time.sleep(10)

###     Fuente 4 - MOVISTAR
print("Scrapping MOVISTAR...")
result = target.getPhonePricesFromMovistar()


# (3) MUESTRO LOS REGISTROS GUARDADOS
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''SELECT * from PHONEPRICES''')
# cursor.execute('''
#     CREATE TABLE PHONEPRICES (
#    SOURCE VARCHAR(255),
#    MODEL VARCHAR(255),
#    PRICE VARCHAR(20)
# )
# ''')
result = cursor.fetchall()
print(result)
conn.close()