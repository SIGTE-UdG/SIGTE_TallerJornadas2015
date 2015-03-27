#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A partir de una capa de polígonos obtendremos indicadores estadísticos de
temperatura por cada polígono.

Importar capa vectorial 'barrios.shp' como 'BARRIOS'


Obtener datos estadíticos (valor mínimo, valor máximo, media) a partir
de la imagen 'LST' y BARRIOS'.
La función a usar es: v.rast.stats
Los parámeteros a  usar son map, raster, method y column_prefix
Usad 'T_' cómo prefijo.

Obtener datos estadíticos (valor mínimo, valor máximo, media) a partir
de la imagen 'LST2' y BARRIOS'.
La función a usar es: v.rast.stats
Los parámeteros a  usar son map, raster, method y column_prefix
Usad 'T2_' cómo prefijo.

"""
print "Ejecutando %s" % __file__

import grass.script as grass


BARRIOS="/home/user/Documentos/datos/barrios/barrios.shp"
#http://grass.osgeo.org/grass70/manuals/v.rast.stats.html
##EJERCICIO## ##EJECUTAR_COMANDO## ##IMPORTAR ARCHIVO VECTORIAL## ##PARÁMETROS##
grass.run_command('v.in.ogr', input=BARRIOS, output='BARRIOS')

#http://grass.osgeo.org/grass70/manuals/v.rast.stats.html
##EJERCICIO## ##EJECUTAR_COMANDO## ##v.rast.stats## ##PARÁMETROS## ##FLAGS c##
grass.run_command('v.rast.stats', map='BARRIOS', raster='LST',
    method='minimum,maximum,average', column_prefix='T_', flags='c')

#http://grass.osgeo.org/grass70/manuals/v.rast.stats.html
##EJERCICIO## ##EJECUTAR_COMANDO## ##v.rast.stats## ##PARÁMETROS## ##FLAGS c##
grass.run_command('v.rast.stats', map='BARRIOS', raster='LST2',
    method='minimum,maximum,average', column_prefix='T2_', flags='c')