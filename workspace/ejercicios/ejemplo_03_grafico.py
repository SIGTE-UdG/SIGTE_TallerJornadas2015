#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A partir de los datos obtenidos en el ejercicio 08 se crea un gráfico.
"""

import os, sys, StringIO,csv
import grass.script as grass

#Leemos los datos de la capa BARRIOS
#http://grass.osgeo.org/grass70/manuals/v.db.select.html
# v.db.select map='BARRIOS' columns='BARRIS,T__minimum,T__maximum,T__average'
datos = grass.read_command('v.db.select', map='BARRIOS',
    columns='BARRIS,T__minimum,T__maximum,T__average,T2__minimum,T2__maximum,T2__average')

#Leemos la salida de texto de grass y ponemos los datos en tres tablas.

barrios = []
minimas = []
maximas = []
medias = []

minimas2 = []
maximas2 = []
medias2 = []


f = StringIO.StringIO(datos)
reader = csv.reader(f, delimiter='|')
i=0
for nombre, tmin, tmax, media, tmin2, tmax2, media2 in reader:
    if i>0:
        barrios.append(nombre)
        minimas.append(float(tmin))
        maximas.append(float(tmax))
        medias.append(float(media))
        minimas2.append(float(tmin2))
        maximas2.append(float(tmax2))
        medias2.append(float(media2))
    i=i+1



#Con los  datos obtenisod creamos el gráfico.
#http://matplotlib.org/api/pyplot_api.html

import numpy as np
import matplotlib.pyplot as plt

ind = np.arange(len(barrios))
ancho_columna = 0.2


plt.plot(ind, minimas, color='blue')
plt.plot(ind+(ancho_columna), medias, color='green')
plt.plot(ind+(ancho_columna*2), maximas, color='brown')

rect_minimas = plt.bar(ind, minimas2, ancho_columna, color='blue')
rect_medias = plt.bar(ind+(ancho_columna), medias2, ancho_columna, color='green')
rect_maximas = plt.bar(ind+(ancho_columna*2), maximas2, ancho_columna, color='brown')





plt.ylabel(u'Temperatura ºC')
plt.title(u'Temperatura del suelo por barrios')

plt.xticks(ind+(ancho_columna/2)*3, barrios, rotation=90)

leyenda = plt.legend( (rect_minimas[0], rect_medias[0], rect_maximas[0]),
    (u'Mínima', u'Media', u'Máxima') )

# fig.legend([line1, line2], ['yep', 'nope'], bbox_to_anchor=[0.5, 0.5],
#            loc='center', ncol=2)


#legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
# Put a nicer background color on the legend.
#legend.get_frame().set_facecolor('#00FFCC')


#Para que no se corten los nombres de los barrios
plt.subplots_adjust(bottom=0.25)

plt.show()

