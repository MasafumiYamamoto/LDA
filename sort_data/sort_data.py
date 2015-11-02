import mkeachbus_d
import ext_d
import mege_d
import calcdis_d
import rank_d
import time

###############
#set variable
##############
rootpath_="D:/Lresult/over4/"
print "tbum"
tnum_=raw_input()
bnum_=6
rflag_=1
tflag_=0
infile_="nNVrev_LSI_o4b6_t"+str(tnum_)+".csv"

print "start",time.ctime()
#mkeachbus_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_,infile_)
print "mkeachbus_d fin",time.ctime()
#ext_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_)
print "ext_d fin",time.ctime()
mege_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_)
print "mege_d fin",time.ctime()
calcdis_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_)
print "calcdis_d fin",time.ctime()
rank_d.main(rootpath_,tnum_,bnum_,rflag_,tflag_)
print "rank_d fin",time.ctime()
