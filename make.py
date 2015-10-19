import time
import mkcorpus_d 
import mkLDAmodel_d

print "start",time.ctime()
mkcorpus_d.mkcorpus()
print "mkcorpus fin",time.ctime()
mkLDAmodel_d.mkLDAmodel()
print "mkLDAmodel fin",time.ctime()
