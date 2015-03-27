#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 6:

Utilizad la calculadora ráster de GRASS para obtener los valores LSE de las bandas 10 y 11.
r.mapcalc "LSE_B10 = 0.971*(1-FVC)+0.987*FVC"
r.mapcalc "LSE_B11 = 0.977*(1-FVC)+0.989*FVC"
"""
print "Ejecutando %s" % __file__

import grass.script as grass


##EJERCICIO## ##EJECUTAR_COMANDO## ##CÁLCULO RÁSTER LSE_B10## ##PARÁMETROS##
grass.run_command('r.mapcalc',
                   expression='LSE_B10 = 0.971*(1-FVC)+0.987*FVC')

##EJERCICIO## ##EJECUTAR_COMANDO## ##CÁLCULO RÁSTER LSE_B11## ##PARÁMETROS##
grass.run_command('r.mapcalc',
                   expression='LSE_B11 = 0.977*(1-FVC)+0.989*FVC')


