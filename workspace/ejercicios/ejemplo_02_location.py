import os

import grass.script as grass

#Print region extent
r = grass.read_command("g.region", flags='p' )
print r