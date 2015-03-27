#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 5:

Utilizad r.info para hallar los valores mínimo y máximo de la capa NDVI.

Utilizad la calculadora ráster de GRASS para obtener el FVC.
r.mapcalc "FVC = ((NDVI+NDVImin)/(NDVImax - NDVImin))^2"
"""
print "Ejecutando %s" % __file__

import grass.script as grass


##EJERCICIO## ##resultado = PARSEAR_COMANDO## ##OBTENER INFORMACIÓN DE NDVI## ##PARÁMETROS## ##FLAGS, r##
resultado = grass.parse_command('r.info', map='NDVI', flags='r')
NDVImin = resultado['min']
NDVImax = resultado['max']

##EJERCICIO## ##EJECUTAR_COMANDO## ##CÁLCULO RÁSTER## ##PARÁMETROS##
grass.run_command('r.mapcalc',
                   expression='FVC = ((NDVI+%s)/(%s - %s))^2'
                   % (NDVImin,NDVImax,NDVImin))
