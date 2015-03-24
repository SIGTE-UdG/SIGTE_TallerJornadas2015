#!/usr/bin/env bash

#http://grasswiki.osgeo.org/wiki/GRASS_and_Python

export GISBASE=/usr/lib/grass70
export GRASS_VERSION="7.0.0"

GISRC="$HOME/.grassrc7"
export GISRC

export GRASS_PYTHON=python

export PATH="$GISBASE/bin:$GISBASE/scripts:$PATH"
export LD_LIBRARY_PATH="$GISBASE/lib"
export GRASS_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"
export PYTHONPATH="$GISBASE/etc/python:$PYTHONPATH"


#generate GISRCRC
MYGISDBASE=$HOME/Documentos/grassdata
MYLOC=catalunya
MYMAPSET=taller
echo "GISDBASE: $MYGISDBASE" > "$GISRC"
echo "LOCATION_NAME: $MYLOC" >> "$GISRC"
echo "MAPSET: $MYMAPSET" >> "$GISRC"


