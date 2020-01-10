#!/usr/bin/env python

"""Extract the htm pixels for the Gaia DR2 refcat on lsst-dev and tarball them.

Run in the directory you want the output to land in on lsst-dev with:
    python gaia_HiTS_2015.py | bash
"""

from esutil import htm 

# field 26 (2014:04) -10:00:28.800 +02:12:36.00
# field 40 (2014:10) -10:20:28.800 -06:31:12.00
# field 42 (2014:09) -10:21:52.800 -04:57:00.00

indexer = htm.HTM(depth=7) 
ras = [15.*(10.+( 0./60.)+(28.800/3600.)), 
       15.*(10.+(20./60.)+(28.800/3600.)), 
       15.*(10.+(21./60.)+(52.800/3600.))] 
decs = [+(2+(12./60.)+(36./3600.)), 
        -(6+(31./60.)+(12.00/3600.)), 
        -(4.+(57./60.))]

shards = []

for ra, dec in zip(ras, decs):
    shards += list(indexer.intersect(ra, dec, 2., True))

print("mkdir ./gaia_HiTS_2015")
print("cp -v /datasets/refcats/htm/v1/gaia_dr2_20191105/config.py ./gaia_HiTS_2015")
print("cp -v /datasets/refcats/htm/v1/gaia_dr2_20191105/master_schema.fits ./gaia_HiTS_2015")
for shard in shards:
    print("cp -v /datasets/refcats/htm/v1/gaia_dr2_20191105/%i.fits ./gaia_HiTS_2015/"%shard)
print("tar cvzf gaia_HiTS_2015.tar.gz -C gaia_HiTS_2015 .")
