##Importo las librerías a utilizar 

import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
import time inicio_este = time.time()

##Tengo que generar dos variables: 
##Una va a tener la URL de la página y otra va a ser la ruta donde se va a guardar mi archivo. 

link = 'https//:…………' 
archivo_guardado = 'C:\\Users\\Desktop\\web_scraping.xlsx'

##Genero las listas donde se va a guardar la información: 

url_estado = [] 
url_precios = [] 
precio = [] 
nombre_de_la_publicacion = []

##Creo la función extraccion_datos 

def extraccion_datos(urls):
  for url in urls: 
    try: 
      nota = requests.get(url) 
      url_estado.append('OK') 
      url_precios.append(url) 
    except Exception as e: 
      url_estado.append(e) 
      url_precios.append(0) 
      precio.append(0) 
      nombre_de_la_publicacion.append(0) 
     
    if nota.status_code !=200: 
      url_estado.append(f'status code = {nota.status_code}') 
      url_precios.append(0) 
      precio.append(0) 
      nombre_de_la_publicacion.append(0)
    
    s_nota = BeautifulSoup(nota.text, 'lxml') 
    
    #extraemos el precio 
    precio_interno = s_nota.find('span', attrs={'class':'andes-money-amount__fraction'}) 
    if precio_interno: 
      precio.append(precio_interno.text) 
    else: precio.append(0) 
    
    #extraemos el nombre de la publicación 
    nombre_de_la_publicacion_interno = s_nota.find('h1', attrs={'class':'ui-pdp-title'}) 
    if nombre_de_la_publicacion_interno: 
      nombre_de_la_publicacion.append(nombre_de_la_publicacion_interno.text) 
    else: nombre_de_la_publicacion.append(0) 
  return print('Se ejecutó correctamente')
