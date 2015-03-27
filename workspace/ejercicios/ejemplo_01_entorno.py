"""Muestra las variables de entorno de GRASS"""

import grass.script as grass

env = grass.gisenv()

print env 
