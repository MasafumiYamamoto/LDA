import mkeachbus_d
import ext_d
import mege_d
import calcdis_d
import rank_d
import time

###############
#set variable
##############
rootpath_="D:/Lresult/NV_s5/"
print "tbum"
tnum_=raw_input()
bnum_=6
rflag_=0
tflag_=0
infile_="NVrev_LDA_o4b6t"+str(tnum_)+".csv"
model_="LDA"

print "start",time.ctime()
mkeachbus_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_,infile_,model_)
print "mkeachbus_d fin",time.ctime()
ext_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_)
print "ext_d fin",time.ctime()
mege_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_)
print "mege_d fin",time.ctime()
calcdis_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_)
print "calcdis_d fin",time.ctime()
rank_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_)
print "rank_d fin",time.ctime()
