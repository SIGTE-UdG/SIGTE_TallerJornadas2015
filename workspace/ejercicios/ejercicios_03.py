#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejercicio 3:

Utilizad el comando de GRASS i.vi para el cálculo de índices de vegetación.Las bandas a utilizar serán las correspondientes al rojo (B4) y al infrarrojo (B5) corregidas atmosféricamente.
i.vi red=B4 corregida atmosféricamente output=NDVI viname=ndvi nir=B5 corregida atmosféricamente
Visualizad el histograma de la imagen correspondiente al NDVI que habéis creado. Los valores debería estar entre el intervalo -1,1.
"""
print "Ejecutando %s" % __file__

import grass.script as grass


##EJERCICIO## ##EJECUTAR_COMANDO## ##CÁLCULO DE ÍNDICES DE VEGETACIÓN## ##PARÁMETROS##
grass.run_command('i.vi', red=u'DOS_4',
                   output='NDVI', viname='ndvi',
                   nir=u'DOS_5')

