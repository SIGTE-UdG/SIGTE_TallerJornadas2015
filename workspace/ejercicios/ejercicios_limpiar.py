#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Elimina todas la capas, tanto de tipo ráster cómo vectoriales.
"""
print "Ejecutando %s" % __file__

import os, sys
import grass.script as grass


excepto = ['LST']

#Leemos las imágenes y las ponemos en un array
imagenes = grass.parse_command('g.list', type='raster').keys()


# Borrar todas las imágenes y la máscara
for imagen in imagenes:
    if imagen not in excepto:
        grass.read_command('g.remove', type='raster', name=imagen, flags='f')

# Las capas vectoriales
capas_vectoriales = grass.parse_command('g.list', type='vector').keys()
for vector in capas_vectoriales:
    if vector not in excepto:
        grass.read_command('g.remove', type='vector', name=vector, flags='f')


