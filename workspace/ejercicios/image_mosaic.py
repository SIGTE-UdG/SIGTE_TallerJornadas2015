import os
import grass.script as grass

#Print region extent
image1='/home/abusquets/sigte/projectes/taller_grass/workspace/datos/LC81980312014340LGN00/LC81980312014340LGN00_B1.TIF'
image2='/home/abusquets/sigte/projectes/taller_grass/workspace/datos/LC81980332014340LGN00/LC81980332014340LGN00_B1.TIF'

r = grass.read_command("i.image.mosaic", image1=image1 image2=image2)

export MAPS=`g.mlist type=rast sep=, pat="map_*"`
g.region rast=$MAPS -p
r.patch in=$MAPS out=mosaic