#
#Llamar a una API es una de las tareas más comunes en programación.#
#Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...#
#Aquí tienes un listado de posibles APIs: 
#https://github.com/public-apis/public-apis
#

import json
import requests

url = "https://newton.now.sh/api/v2/factor/x^2-1"
response = requests.get(url)
print(response.text)