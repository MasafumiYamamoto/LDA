import mkeachbus_d
import textedit
import mkcorpus_d
import mkmodel_d
import calcsim_d
import time
import os

###############
#set variable
##############
model_="lda"
bnum_=6
print "tnum"
tnum_=int(raw_input())
train_="NVreview"
pas_=os.getcwd()
pas_=pas_+"/"

print "start",time.ctime()
#mkcorpus_d.main(model_,bnum_,tnum_,train_,pas_)
print "mkcorpus_d fin",time.ctime()
mkmodel_d.main(model_,bnum_,tnum_,train_,pas_)
print "mkmodel_d fin",time.ctime()
calcsim_d.main(model_,bnum_,tnum_,train_,pas_)
print "calc 1 fin"
model_="lsi"
calcsim_d.main(model_,bnum_,tnum_,train_,pas_)
print "calcsim_d fin",time.ctime()
