#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TODO: descripción
"""

import os, sys, StringIO,csv
import grass.script as grass

#Leemos los datos de la capa BARRIOS

#http://grass.osgeo.org/grass70/manuals/v.db.select.html
# v.db.select map='BARRIOS' columns='BARRIS,T__minimum,T__maximum,T__average'
datos = grass.read_command('v.db.select', map='BARRIOS', 
    columns='BARRIS,T__minimum,T__maximum,T__average')


#Leemos la salida de texto de grass y pomemos los datos en tres tablas.

barrios = []
minimas = []
maximas = []
medias = []

f = StringIO.StringIO(datos)
reader = csv.reader(f, delimiter='|')
i=0
for nombre, tmin, tmax, media in reader:
    if i>0:
        barrios.append(nombre)
        minimas.append(float(tmin))
        maximas.append(float(tmax))
        medias.append(float(media))
    i=i+1



#Creamos un gráfico.
#http://matplotlib.org/api/pyplot_api.html

import numpy as np
import matplotlib.pyplot as plt

ind = np.arange(len(barrios))


width = 0.2

# fig = plt.figure()
# ax = fig.add_subplot(111)

rect_minimas = plt.bar(ind, minimas, width, color='blue')
rect_medias = plt.bar(ind+(width), medias, width, color='green')
rect_maximas = plt.bar(ind+(width*2), maximas, width, color='brown')


plt.ylabel(u'Temperatura ºC')
plt.title(u'Temperatura del suelo por barrios')
# plt.set_xticks(ind+width)
# plt.set_xticklabels(barrios, rotation=90)

plt.legend( (rect_minimas[0], rect_medias[0], rect_maximas[0]), 
    (u'Mínima', u'Media', u'Máxima') )

plt.show()









# 
# plt.set_xlabel('Barrios')
# plt.set_ylabel(u'Temperatura ºC')
# 
# plt.show()
#plt.plot([1,2,3,4])
# plt.plot([1,2,3,4], [1,4,9,16])
# plt.ylabel('some numbers')
# plt.show()


import numpy as np
# x = linspace(0,5,50)
# y = x**2
# 
# fig = plt.figure()
# 
# ejes = plt.add_axes([0.1, 0.1, 0.8, 0.8]) # izquierda, abajo, ancho, altura (rango 0 a 1)
# ejes.plot(x,y,'r')
# ejes.set_xlabel('Barrios')
# ejes.set_ylabel(u'Temperatura ºC')
# ejes.set_title(u'Temperatura de la superfície terrestre por barrios');
# plt.show()

# means_men = (20, 35, 30, 35, 27)
# std_men = (2, 3, 4, 1, 2)
# 
# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)
# 
# fig, ax = plt.subplots()
# 
# index = np.arange(n_groups)
# bar_width = 0.35
# 
# opacity = 0.4
# error_config = {'ecolor': '0.3'}
# 
# rects1 = plt.bar(index, means_men, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  yerr=std_men,
#                  error_kw=error_config,
#                  label='Men')
# 
# # rects2 = plt.bar(index + bar_width, means_women, bar_width,
# #                  alpha=opacity,
# #                  color='r',
# #                  yerr=std_women,
# #                  error_kw=error_config,
# #                  label='Women')
# 
# plt.xlabel(u'Barrios')
# plt.ylabel(u'Temperatura ºC')
# plt.title(u'Temperatura de la superfície terrestre por barrios')
# plt.xticks(len(barrios), barrios)
# 
# plt.legend()
# 
# plt.tight_layout()
# plt.show()





    