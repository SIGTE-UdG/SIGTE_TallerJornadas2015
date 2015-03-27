#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 7:

Utilizad la calculadora raster de GRASS para obtener los valores
correspondientes a al valor medio LSE y a la diferencia en LSE.

La imagen de destino debe de ser LST2

Para pasar de °K a °C
°C=°K-273.15
"""
print "Ejecutando %s" % __file__

import grass.script as grass


##EJERCICIO## ##EJECUTAR_COMANDO## ##CÁLCULO RÁSTER LST2## ##PARÁMETROS##
expression="LST2 = (" \
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
