#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TODO: descripción
"""

import os, sys
import grass.script as grass



#Importamos la capa que contiene nuestros polígonos
#Primero borramos la capa si la tenemos dades de alta BARRIOS
grass.run_command('g.remove', type='vect', name='BARRIOS', flags='f')
BARRIOS="/home/usuario/Documentos/taller_grass/workspace/datos/barrios/barrios_copia.shp"
grass.run_command('v.in.ogr', input=BARRIOS, output='BARRIOS', flags='o')


#http://grass.osgeo.org/grass70/manuals/v.rast.stats.html
grass.run_command('v.rast.stats', map='BARRIOS', raster='LST',
    method='minimum,maximum,average', column_prefix='T_', flags='c')

datos = grass.read_command('v.db.select', map='BARRIOS', 
    columns='NOM_COMPLE,T__minimum,T__maximum,T__average')


import StringIO
import csv

f = StringIO.StringIO(datos)
reader = csv.reader(f, delimiter='|')
for row in reader:
    print '\t'.join(row)
    




    