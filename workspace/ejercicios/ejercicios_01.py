#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 1:

Utilizad i.landsat.toar de GRASS para obtener la temperatura de brillo a la altura de la atmósfera a partir de las bandas térmicas de la imagen.
El método uncorrected at-sensor values de i.landsat.toar convierte los ND de la imagen a valores de radiancia, y posteriormente a reflectividad. Las bandas térmicas se convierten en primer lugar a valores de radiancia, y posteriormente a valores de temperatura a la altura del sensor, en grados Kelvin.
i.landsat.toar input=PREFIJO DE LAS BANDAS output=PREFIJO DE SALIDA metafile=RUTA AL FICHERO DE METADATOS sensor=oli8
"""
print "Ejecutando %s" % __file__

import grass.script as grass


DIRECTORIO_IMAGENES="/home/user/Documentos/taller_grass/workspace/datos/LC81970312014253LGN00"
prefijo_imagen = DIRECTORIO_IMAGENES.split('/')[-1]

print "Ejercicio 1"
archivo_metfile = "%s/%s_MTL.txt" % (DIRECTORIO_IMAGENES, prefijo_imagen)
##EJERCICIO## ##EJECUTAR_COMANDO## ##OBTENER TEMPERATURA DE BRILLO## ##PARÁMETROS##
grass.run_command('i.landsat.toar', input='%s_B' % prefijo_imagen,
                   output='REF_',
                   metfile=archivo_metfile, sensor='oli8')
