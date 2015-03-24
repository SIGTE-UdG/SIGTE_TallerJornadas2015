#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import grass.script as grass

#Borrar todas las mascaras
DIRECTORIO_IMAGENES="/home/usuario/Documentos/taller_grass/workspace/datos/LC81970312014253LGN00"
SHP_RECORTAR="/home/usuario/Documentos/taller_grass/workspace/datos/mascara.shp"
prefijo_imagen = DIRECTORIO_IMAGENES.split('/')[-1]

#Leemos las imágenes y las ponemos en un array
imagenes = grass.parse_command('g.list', type='raster').keys()
## Otra forma
# imagenes = grass.read_command('g.list', type='raster').split('\n')
# if imagenes[-1]=='': imagenes.pop(-1)


#Borramos la mascara que tengamos
if 'MASK' in imagenes:
    grass.read_command('g.remove', type='raster', name='MASK', flags='f')


# Borrar todas las imagenes
for imagen in imagenes:
    grass.read_command('g.remove', type='raster', name=imagen, flags='f')

imagenes = []

imagenes_base = []

#Importaremos cada imagen que encontramos en el directorio
for fn in os.listdir(DIRECTORIO_IMAGENES):
    archivo = fn.decode('utf-8')
    if archivo.endswith('.TIF'):
        imagen = "%s/%s" % (DIRECTORIO_IMAGENES, archivo)
        #nombre = archivo
        nombre = archivo.replace('.TIF', '')

        imagenes_base.append(nombre)
        #Importamos la imagen si no existe
        if nombre not in imagenes:
            try:
                #Importamos la imagen
                grass.run_command('r.in.gdal', input=imagen, output=nombre)
            except:
                print "No se ha podido importar la imagen %s" % imagen

#Establecemos la región con la primera imagen
grass.run_command('g.region', rast=imagenes_base[0])


#Aplicamos una mascara con los límites de Girona
imagenes = grass.parse_command('g.list', type='raster').keys()
#Borramos la mascara que tengamos
if 'MASK' in imagenes:
    grass.read_command('g.remove', type='raster', name='MASK', flags='f')

grass.run_command('v.in.ogr', input=SHP_RECORTAR, output='LIMITES_TRABAJO', overwrite=True)
grass.run_command('r.mask', vect='LIMITES_TRABAJO')

#Borramos las imágenes no base
for imagen in imagenes:
    if imagen not in imagenes_base:
        grass.read_command('g.remove', type='raster', name=imagen, flags='f')


#Ejercicio 1
print "## Ejercicio 1"
metfile = "%s/%s_MTL.txt" % (DIRECTORIO_IMAGENES, prefijo_imagen)
grass.run_command('i.landsat.toar', input='%s_B' % prefijo_imagen,
                   output='REF_',
                   metfile=metfile, sensor='oli8')


#Ejercicio 2
print "## Ejercicio 2"
grass.run_command('i.landsat.toar', input='%s_B' % prefijo_imagen,
                   output='DOS_',
                   metfile=metfile, method='dos1')


#Ejercicio 3
print "## Ejercicio 3"
grass.run_command('i.vi', red=u'DOS_4',
                   output='NDVI', viname='ndvi',
                   nir=u'DOS_5')

#Ejercicio 4
print "## Ejercicio 4"
grass.run_command('r.colors', map='NDVI', color='ndvi')


#Ejercicio 5
print "## Ejercicio 5"
resultado = grass.parse_command('r.info', map='NDVI', flags='r')
NDVImin = resultado['min']
NDVImax = resultado['max']

grass.run_command('r.mapcalc',
                   expression='FVC = ((NDVI+%s)/(%s - %s))^2'
                   % (NDVImin,NDVImax,NDVImin), overwrite=True)

#Ejercicio 6
print "## Ejercicio 6"
grass.run_command('r.mapcalc',
                   expression='LSE_B10 = 0.971*(1-FVC)+0.987*FVC')
grass.run_command('r.mapcalc',
                   expression='LSE_B11 = 0.977*(1-FVC)+0.989*FVC')


#Ejercicio 7
print "## Ejercicio 7"
#LST = TB10+ C1(TB10-TB11) + C2(TB10-TB11)2+ C0+(C3+C4W) (1-ε) + (C5+C6W) ∆ ε
expression="LST = (" \
"REF_10" \
" + (1.378 * (REF_10 - REF_11))" \
" + (0.183 * (REF_10 - REF_11)^2)" \
" - " \
" 0.268" \
" + " \
" (54.300-2.238*0.013) * (1 - ((LSE_B10+LSE_B11)/2))" \
" + " \
" (-129.20 + 16.40*0.013) * (LSE_B10 - LSE_B11)" \
") - 273.15"

grass.run_command('r.mapcalc', expression=expression)
