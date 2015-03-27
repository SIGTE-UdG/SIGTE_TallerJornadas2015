#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 2:

Aplicad el método de corrección atmosférica DOS1 a las bandas de la imagen Landsat 8, dejando por defecto los valores correspondientes a Percent of solar radiance y Minimum pixels to consider digital number as dark object.
i.landsat.toar input=PREFIX output=PREFIX metfile=ARCHIVO MET method=dos1
"""
print "Ejecutando %s" % __file__

import grass.script as grass


DIRECTORIO_IMAGENES="/home/user/Documentos/taller_grass/workspace/datos/LC81970312014253LGN00"
prefijo_imagen = DIRECTORIO_IMAGENES.split('/')[-1]


archivo_metfile = "%s/%s_MTL.txt" % (DIRECTORIO_IMAGENES, prefijo_imagen)
##EJERCICIO## ##EJECUTAR_COMANDO## ##CORRECCIÓN ATMOSFERICA## ##PARÁMETROS##
grass.run_command('i.landsat.toar', input='%s_B' % prefijo_imagen,
                   output='DOS_',
                   metfile=archivo_metfile, method='dos1')

