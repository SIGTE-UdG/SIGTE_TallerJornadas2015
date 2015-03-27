#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 0:

Utilizad el comando r.in.gdal para importar todas las bandas de la imagen.

"""
print "Ejecutando %s" % __file__

import os, sys
import grass.script as grass


DIRECTORIO_IMAGENES="/home/user/Documentos/taller_grass/workspace/datos/LC81970312014253LGN00"
SHP_RECORTAR="/home/user/Documentos/taller_grass/workspace/datos/mascara.shp"
prefijo_imagen = DIRECTORIO_IMAGENES.split('/')[-1]

imagenes_base = []

#Importaremos cada imagen que encontramos en el directorio
for fn in os.listdir(DIRECTORIO_IMAGENES):
    archivo = fn.decode('utf-8')
    if archivo.endswith('.TIF'):
        imagen = "%s/%s" % (DIRECTORIO_IMAGENES, archivo)
        nombre = archivo.replace('.TIF', '')

        imagenes_base.append(nombre)

        try:
            #Importamos la imagen
            ##EJERCICIO## ##EJECUTAR_COMANDO## ##IMPORTAR IMAGEN RÁSTER## ##PARÁMETROS##

        except:
            print "No se ha podido importar la imagen %s" % imagen

#Establecemos la región con la primera imagen.
grass.run_command('g.region', rast=imagenes_base[0])


#Cargamos una máscara para hagilizar los cálculos.
grass.run_command('v.in.ogr', input=SHP_RECORTAR, output='LIMITES_TRABAJO', overwrite=True)
grass.run_command('r.mask', vect='LIMITES_TRABAJO')