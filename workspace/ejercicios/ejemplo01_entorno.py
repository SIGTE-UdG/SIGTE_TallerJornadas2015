"""Muestra las variables de entorno de grass"""

import os

import grass.script as grass

env = grass.gisenv()

for key, value in os.environ.items(): 
    print key, value