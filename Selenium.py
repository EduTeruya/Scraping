''' La aplicacion es una prueba de concepto sobre mi proyecto de tesis sabado en webscraping.
Para ello he utilizado selenium que es un framework para aplicaciones web que facilita la automatizacion
Tambien webdriver la cual es una interfaz para simular interacciones de un usuario con cualquier navergador, en este caso Chrome
Lo que hace esta aplicacion es inicialmente abrir la pagina web https://www.adamchoi.co.uk/teamgoals/detailed que es una pagina de estadisticas
de futbol y dentro de ella seleccionar el elemento (All matches) y darle click.
Luego dentro del dropdown llamado (Country), selecciona el pais (Spain).
Finalmente, toda la informacion que aparece sobre los partidos, los cuales tienen como tag (tr) es listada y con la libreria pandas es impresa para mostrar
los resultados. Tambien es guardada en un archivo CSV.

Como presentacion final se busca que la aplicacion haga scraping simultaneamente a varias paginas web. En este caso sera orientado a empresas
de telefonica celular, con lo cual se podra obtener informacion de los precios de los planes y los celulares de distinatas empresas como Claro,
Movistar o Entel; y poder mostrar una comparativa, ya sea la variacion porcentual de los precios de X celular por empresa o la variacion del precio
en valor monetario, para poder ver de manera sencilla cual alternativa es mas economica.

La finalidad es reducir los tiempos de respuesta de los usuarios para la eleccion de un producto, en este caso la compra de una celular.
La aplicacion les brinda la informacion de precios y comparativa, por lo cual los usuarios solo tendrian que tomar la desicion de compra y no
tener que gastar tiempos innecesarios en buscar todas las alternativas del mercado, ya que el programa lo hace por ellos.

'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
patch = '/Users/51987/Desktop/WebScraping/chromedriver'

# Uso de webdriver para iniciar la pagina web seleccionada
driver = webdriver.Chrome(patch)
driver.get(website)

# Selecciona el elemento "All Matches" y le da click
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

# Selecciona el pais Spain dentro del dropdown seleccionado
dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

# Da 5 segundos de espera para continuar con la siguiente funcion
time.sleep(5)

matches = driver.find_elements_by_tag_name('tr')

# Lista los elementos 
partidos = []
for match in matches:
    partidos.append(match.text)

#(Quitar el comentario para activar) driver.quit()

#Pandas
df = pd.DataFrame({'partidos': partidos})
print(df)


df.to_csv('partidos.csv', index=False)
