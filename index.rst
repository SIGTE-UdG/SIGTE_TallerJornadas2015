.. taller SIGTE documentation master file, created by
   sphinx-quickstart on Fri Jan 30 18:35:02 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



TALLER TELEDETECCIO
==================

GRASS, PYTHON...
alex, pep
divendres

Índice del taller
=================
1. Breve introducción a la teledetección
2. ¿Qué módulos nos ofrece GRASS Gis para trabajar con imágenes de satélite?
3. Correcciones atmosféricas de imagenes de satélite
4. Calculo de temperaturas a partir de imagenes de satélite
5. Scripts de python sobre GRASS Gis aplicados a la teledetección
 

¿Qué es la teledetección?
==========================
El término teledetección hace referencia a las distintas formas de adquirir información de forma remota a través
de sensores sin entrar en contacto físico con el objeto. Los sensores se localizan en plataformas de observación (bien en aviones o satélites), y registran la información centrada en las regiones del espectro electromagnético. La teledetección tiene como objetivo
obtener las características de la superficie observada y los fenómenos que en ella tienen lugar. Distintas disciplinas se sirven de
esta fuente de información (meteorología, oceanografía, geología, geografía,...), por lo que esta nueva forma de ver nuestro planeta viene acompañada por el desarrollo de potentes modelos físico-matemáticos que tratan de describir los procesos físicos que tienen lugar en nuestro entorno.

.. figure:: img/tele1.jpeg
   :align:  center
   :width: 450pt



El programa Landsat
====================
Vamos a desarrollar el taller utilizando imagenes del satélite **Landsat**. 

Desde que a finales de la década de los 60 la agencia espacial norteamericana diseñó el primer proyecto dedicado exclusivamente a la observación de los recursos terrestres, la família Landsat ha constituido el proyecto más fructífero de teledetección espacial desarrollado hasta el momento. 

La buena resolución de sus sensores, el carácter global y periódico de la observación que realizan y la buena comercialización, explican su profuso empleo por experts de muy variados campos en todo el mundo. 

Con el **Landsat 8** (cuyo nombre técnico es LCDM 'Landsat Data Continuity Mission') se ha dado continuidad al programa más largo de la historia sobre información del planteta. 


El sensor OLI (Operational Land Imager)
_______________________________________

A bordo del Landsat 8, se encuentra el sensor OLI, puesto en órbita en Febrero del 2013. Las bandas espectrales capturadas por este sensor son muy parecidas a las del sensor ETM+ (a bordo del Landsat 7), aunqué se han añadido dos de nuevas: un nuevo **canal en azul visible** (banda 1) disseñado especificamente para observar la calidad del agua en lagos someros y zonas costeras, así como para detectar aerosoles, y otro **canal en el infrarrojo** (banda 9) para determinar la presencia de nubes -fundamentalmente cirrus-. 

Asimismo, junto a acada escena del Landsat 8 se incluye también una banda de valoración de calidad (*Quality Assurance band*), que ofrece información respecto anomalías en la toma de datos por problemas en el instrumental o la presencia de elementos como nubes, agua y nieve. 

El sensor TIRS (Thermal Infrarred Sensor)
_________________________________________

El sensor TIRS capta información acerca la temperatura de la superficie terrestre a través de dos bandas del infrarroje térmico (banda 10 y banda 11). Permite distinguir entre la temperatura de la superficie terrestre y la temperatura atmosfércia. Tienen una resolución de 100 mts. 


Las bandas del satélite Landsat 8
_________________________________


+-------+------------------------+------------+----------+
| Sensor|Band Number             | Amplitud   |Resolución|    
+=======+========================+============+==========+
| Oli   |1. Coastal aerosol      |0,43-0,45μm |30m       |  
+-------+------------------------+------------+----------+
|       |2. Blue                 |0,45-0,51μm |30m       |  
+-------+------------------------+------------+----------+
|       |3. Green                |0,53-0,59μm |30m       |  
+-------+------------------------+------------+----------+
|       |4. Red                  |0,64-0,67μm |30m       |  
+-------+------------------------+------------+----------+
|       |5. Near Infrared (NIR)  |0,85-0,88μm |30m       |  
+-------+------------------------+------------+----------+
|       |6. SWIR 1               |1,57-1,65μm |30m       |  
+-------+------------------------+------------+----------+
|       |7. SWIR 2               |2,11-2,29μm |30m       |  
+-------+------------------------+------------+----------+
|       |8. Panchromatic         |0,50-0,68μm |30m       |  
+-------+------------------------+------------+----------+
|       |9. Cirrus               |1,36-1,38μm |30m       |  
+-------+------------------------+------------+----------+
|TIRS   |10. Thermal Infrarred 1 |10,6-11,9μm |100m      |  
+-------+------------------------+------------+----------+
|       |11. Thermal Infrarred 2 |11,5-12,51μm|100m      |  
+-------+------------------------+------------+----------+




Cálculo de la temperatura terrestre (LST) utilizando las bandas del TIRS
=========================================================================



Split-window algorithm 
_______________________

Para el cálculo de la temperatura de la superfície, se utilizará el algoritmo Split-Window (SW). Se trata del algoritmo maś utilizado para el cálculo de LST debido a su simplicidad y robustez. 

Este algoritmo se basa en el hecho que la radiación absorvida por la atmósfera es proporcional a la diferencia de brillo entre las mediciones simultáneas en dos lonigudes de onda diferentes, correspondientes a las dos bandas del sensor TIRS. 


LST = TB\ :sub:`10`\ + C\ :sub:`1`\ (TB\ :sub:`10`\-TB\ :sub:`11`\ ) + C\ :sub:`2`\ (TB\ :sub:`10`\ -TB\ :sub:`11`\ )2+ C\ :sub:`0`\ +(C\ :sub:`3`\ +C\ :sub:`4`\ W) (1-ε) + (C\ :sub:`5`\ +C\ :sub:`6`\ W) ∆ ε



donde:

LST - Land Surface Temperature (Kelvin)

C\ :sub:`0`\  to  C\ :sub:`6`\ - Valores del coeficiente para SW (Skokovic et al, 2014; Sobrino et al, 1996; Shaouhua Zhao et al, 2009)

+------------+------+
| Constant   |Value |    
+============+======+
|C\ :sub:`0` |-0.268|
+------------+------+
|C\ :sub:`1` |1.378 |
+------------+------+
|C\ :sub:`2` |0.183 |
+------------+------+
|C\ :sub:`3` |54.300|
+------------+------+
|C\ :sub:`4` |-2.238|
+------------+------+
|C\ :sub:`5` |-129.2|
+------------+------+
|C\ :sub:`6` |16.400|
+------------+------+




TB\ :sub:`10`\ y TB\ :sub:`11`\ - temperatura de brillo de la banda 10 y 11 (K)

∆ - valor medio LSE (Land Surface Emissivity) de las bandas del TIR

W - contenido de vapor de agua en la atmósfera

∆ ε - Diferencia en LSE

.. seealso::
      **Estimation of Land Surface Temperature of Dindigul district using Landsat 8 Data** (2014). Rajeshwari A, Mani N D. International Journal of Research in Engineering and Technology.

Convertir los ND a valores de radiancia (TOA - Top of athmosphere)
___________________________________________________________________
 
A partir de los datos medidos por el sensor, puede obtenerse la **energía reflejada**, ya que la radiancia espectral medida por éste es consecuencia de la reflexión de la radiación electromagnética en las cubiertas. Esta reflexión se codifica con un valor numérico, que se denomina **ND**, de acuerdo a los coeficientes de calibración específicos para cada sensor. Dada que estos coeficientes son conocidos, puede realizarse el proceso inverso, obteniendo así los valores de **radiancia** espectral detectado por el sensor a partir de los ND. 


Para aplicar la fórmula del SW *algorithm*, es imprescindible conocer estos valores de radiancia. 
Las bandas del sensor OLI y TIRS pueden convertirse a valores de radiancia espectral del siguiente modo: 

Lλ = MLQcal + AL 

donde:              

Lλ = TOA spectral radiance (Watts/( m2 * srad * μm))

ML = Band-specific multiplicative rescaling factor from the metadata (RADIANCE_MULT_BAND_x, where x is the band number)
    
AL = Band-specific additive rescaling factor from the metadata (RADIANCE_ADD_BAND_x, where x is the band number)
    
Qcal = Quantized and calibrated standard product pixel values (DN)  



Conversión a valores de reflectividad aparente y temperatura de Brillo a la altura de la atmósfera (TOA)
__________________________________________________________________________________________________________

A partir de los valores de radiancia, utilizando las bandas térmicas fácilmente se puede derivar la temperatura a la altura del sensor. 
Las bandas del TIRS se pueden convertir a temperatura de brillo utilizando las constantes que figuran en el archivo de metadatos. De este modo:

.. figure:: img/tele2.png
   :align:  center
   :width: 100pt


donde:              

T = At-satellite brightness temperature (K)

Lλ = TOA spectral radiance (Watts/( m2 * srad * μm))

K1 = Band-specific thermal conversion constant from the metadata (K1_CONSTANT_BAND_x, where x is the band number, 10 or 11)

K2 = Band-specific thermal conversion constant from the metadata (K2_CONSTANT_BAND_x, where x is the band number, 10 or 11)


Abrid el archivo de metadatos de la imagen (.met) con un editor de texto, y comprobad que figuran todos los parámetros para el cálculo de la reflectividad: **date, sun_elevation, product_date, gain**.


.. note:: **Ejercicio 1**

   Cread un nuevo location y mapset de GRASS, utilizando el mismo SR que la imagen Landsat 8.

   Utilizad el comando **r.in.gdal** para importar todas las bandas de la imagen. 

   Utilizad **i.landsat.toar** de GRASS para obtener la temperatura de brillo a la altura de la atmósfera a partir de las bandas térmicas de la imagen.

   El método **uncorrected at-sensor values** de i.landsat.toar convierte los ND de la imagen a valores de radiancia, y posteriormente a reflectividad. Las bandas térmicas se convierten en primer lugar a valores de radiancia, y posteriormente a valores de temperatura a la altura del sensor, en grados Kelvin. 
   

  i.landsat.toar input=PREFIJO DE LAS BANDAS output=PREFIJO DE SALIDA metafile=RUTA AL FICHERO DE METADATOS sensor=oli8
   
   *Si se añade* **-r**, *se obtendrán valores de radiancia en vez de valores de reflectividad*. 


Corrección atmosférica
______________________

Este método, no obstante, **no tiene en consideración las influencias atmosféricas** y asume un **terreno plano** y una **observación vertical**, lo cual supone una simplificación de la realidad. De ahí que debamos hablar de reflectividad aparente, pues el valor calculado representa sólo la reflectividad captada por el sensor, pero no la realmente medible en la superficie. 

En cuanto a la **observación vertical**, es asumible para la mayor parte de los sensores de interés ambiental (Landsat, IRS, MOS-MESSR...), pero debe considerarse cuando la adquisición no es vertical, como ocurre con el SPOT-HRV.

Por otro lado, la influencia atmosférica no afecta por igual a los dos componentes del cálculo de la reflectividad (energía reflejada e incidente), ya que el espesor de la atmósfera que atraviesan es distinto. Además, hay que considerar que a la radiancia solar directa hay que añadir la difusa, procedente de otros objetos vecinos. 
Por ello, la radiancia que recibe el satélite no es la misma que la qque sale del suelo, que es la que interesa, dado que pretendemos medir la reflectividad de la cubierta, no la influida por la atmósfera.

Existen distintos procedimientos para abordar las influencias atmosféricas, y determinar la radiancia del suelo, no la que recibe el satélite. 
Desde GRASS, disponemos del módulo **i.landsat.toar** que permite aplicar el método de corrección **DOS** (Dark Object Substraction), y **i.atcorr**, para aplicar el método **6S** (Second Simulation of Satellite Signal in the Solar Spectrum).  

Por su sencillez, utilizaremos el método DOS, que consiste en suponer que el mínimo valor de ND debe corresponder a las zonas oscuras presentes en la imagen y que en ausencia de efecto atmosférico ese valor debería ser cero. Conforme a esta suposición, se deduce que las diferencias entre el cero y los valores mínimos de los histogramas de las distintas bandas afectadas se deben al incremento de la radiancia absorvida por el sensor como consecuencia de la radiación difusa de la atmósfera. El procedimiento de corrección consiste en restar de todos los ND de cada banda, el ND mínimo de ella, de modo que se haga coincidir con el cero del origen del histograma.  

Existen algunas variantes del método de corrección atmosférica DOS (DOS1, DOS2, DOS3 y DOS4)

.. seealso::
      **Classification and Change Detection Using Landsat TM Data: When and How to Correct Atmospheric Effects** (2000). Remote Sensing Environment.

.. note:: **Ejercicio 2**

   Aplicad el método de corrección atmosférica DOS1 a las bandas de la imagen Landsat 8, dejando por defecto los valores correspondientes a **Percent of solar radiance** y **Minimum pixels to consider digital number as dark object**.

   i.landsat.toar input=PREFIX output=PREFIX metfile=ARCHIVO MET method=dos1

   El proceso puede demorarse algunos minutos. 

http://gis.stackexchange.com/questions/40531/how-to-determine-aerosol-model-value-for-i-atcorr-in-grass

Cálculo de valores de emisividad de la superfície terrestre
___________________________________________________________

Otro de los parámetros del **SW algorithm** que es necesario obtener, es el de la emissividad de la superfície terrestre. 
Para entender que es la **emisividad**, hay que hacer referencia previamente a la **emitancia**.

.. note:: Emitancia y Emisividad

   
   Se entiende por **emitancia** el total de energía radiada en todas las direcciones desde una unidad de área y por unidad de tiempo. Se mide en vatios por metro cuadrado.

   La **emisividad** es la relación entre la emitancia de una superfície (M) y la que ofrecería un emisor perfecto, denominado cuerpo negro, a la misma temperatura.

A partir de Índice de Vegetación de Diferencia Normalizada **(NDVI)** es posible derivar el valor de emisividad de las cubiertas del suelo. 

.. seealso::
      **Mapping Land Surface Emissivity from NDVI: Application to European, African, and South American Areas** (1996). Enric Valor and Vicente Caselles. Elsevier Science Inc.
 
**El índice de Vegetación de Diferencia Normalizada**

El Índice de Vegetación de Diferencia Normalizada, también conocido como NDVI por sus siglas en inglés, es uno de los índices más importantes y más ampliamente utilizados.

La fórmula para la obtención de este índice es la siguiente:

**NDVI = (IR – R) / (IR + R)**

donde R e IR son las reflectancias correspondientes al rojo (Banda 4) e infrarrojo (Banda 5) respectivamente.

Los valores resultantes de este índice se encuentran dentro del intervalo (-1,1), indicando los valores altos la presencia de vegetación. 


(NDVI < 0), correspondientes a agua o cubiertas artificiales

(0 < NDVI < 0,2), correspondientes a suelo desnudo o vegetación muerta

(0,2 < NDVI < 0,4), correspondientes a vegetación dispersa o poco vigorosa

(0,4 < NDVI < 0,6), correspondientes a vegetación abundante y vigorosa

(NDVI > 0,6), correspondientes a vegetación muy densa y vigorosa,


.. note:: **Ejercicio 3**

   Utilizad el comando de GRASS **i.vi** para el cálculo de índices de vegetación.Las bandas a utilizar serán las correspondientes al rojo (B4) y al infrarrojo (B5) corregidas atmosféricamente. 

   i.vi red=B4 corregida atmosfericamente output=NDVI viname=ndvi nir=B5 corregida atmosféricamente

   Visualizad el histograma de la imagen correspondiente al NDVI que habéis creado. Los valores debería estar entre el intervalo -1,1.

.. figure:: img/tele3.png
   :align:  center
   :width: 350pt

.. note:: **Ejercicio 4**

   Aplicad una paleta de color específica para la representación de capas NDVI

   r.colors map=NDVI color=ndvi

**Fractional Vegetation Cover (FVC)**
El FVC es un índice que permite estimar la fracción de superfície ocupada por vegetación, y se obtiene a partir del NDVI. 
Obtener el FVC es necesario para hallar los valores de LSE. 

.. figure:: img/tele4.png
   :align:  center
   :width: 250pt


.. note:: **Ejercicio 5**

   Utilizad la calculadora raster de GRASS para obtener el FVC
   Podéis utilizar r.info para hallar los valores mínimo y máximo de la capa NDVI.

   r.mapcalc "FVC = ((NDVI+NDVImin)/(NDVImax - NDVImin))^2"


**Land Surface Emissivity**

Finalmente, podréis obtener los valores correspondientes a LSE para las bandas del sensor TIRS (Band 10 y Band 11), teniendo en consideración que:

.. figure:: img/tele5.png
   :align:  center
   :width: 150pt

donde:

.. figure:: img/tele6.png
   :align: center
   :width: 150pt

+------------+-------+--------+
| Emissivity |Band 10|Band 11 |  
+============+=======+========+
|Soil        |0.971  |0.977   |
+------------+-------+--------+
|Vegetation  |0.987  |0.989   |
+------------+-------+--------+
Fuente: Skokovic et al, 2014; Sobrino et al, 1996; Shaouhua Zhao et al, 2009.

.. note:: **Ejercicio 6**

   Utilizad la calculadora raster de GRASS para obtener los valores LSE de las bandas 10 y 11.

   r.mapcalc "LSE_B10 = 0.971*(1-FVC)+0.987*FVC"

   r.mapcalc "LSE_B11 = 0.977*(1-FVC)+0.989*FVC"


Aplicación del Split-Window Algorithm
______________________________________

Recordad que el SW Algorithm que vamos a aplicar, es:

LST = TB\ :sub:`10`\ + C\ :sub:`1`\ (TB\ :sub:`10`\-TB\ :sub:`11`\ ) + C\ :sub:`2`\ (TB\ :sub:`10`\ -TB\ :sub:`11`\ )2+ C\ :sub:`0`\ +(C\ :sub:`3`\ +C\ :sub:`4`\ W) (1-ε) + (C\ :sub:`5`\ +C\ :sub:`6`\ W) ∆ ε

En este moment, ya únicamente nos faltan los parámetros correspondientes a:

∆ - valor medio LSE (Land Surface Emissivity) de las bandas del TIR = (LSE\ :sub:`10`\ + LSE\ :sub:`11`\) / 2

∆ ε - Diferencia en LSE = LSE\ :sub:`10`\ - LSE\ :sub:`11`\

.. note:: **Ejercicio 7**

   Utilizad la calculadora raster de GRASS para obtener los valores correspondientes a al **valor medio LSE** y a la **diferencia en LSE**.


ref_B10@PERMANENT+1.378*( ref_B10@PERMANENT - ref_B11@PERMANENT)+0.183*( ref_B10@PERMANENT - ref_B11@PERMANENT ) ^2-0.268+ (54.300-2.238*0.013 )*(1- LSE_valorMedio@PERMANENT)+(-129.20+16.40*0.013)* ( LSE_B10@PERMANENT - LSE_B11@PERMANENT     

http://ladsweb.nascom.nasa.gov/data/search.html


