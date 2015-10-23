import csv
import glob
import numpy
import collections

print "file pass"
spas=raw_input()
print "topicnum"
topicnum=int(raw_input())

rfile=open("subrev_1000.csv","r")
rdata=csv.reader(rfile)
rdata.next()
rlist=collections.Counter()
for line in rdata:
    rlist[line[0]]=1
print "rlist",len(rlist)

wfile=open("mergeLDA_r"+str(topicnum)+".csv","wb")
writer=csv.writer(wfile)
header=["bus_id"]
for num in range(0,int(topicnum)):
    header.append("t"+str(num).zfill(2))
writer.writerow(header)
slist=glob.glob(spas+"/*")
subnum=0
for shop in slist:
    wlist=[]
    tlist=numpy.array([0]*topicnum)
    ifile=open(shop,"r")
    idata=csv.reader(ifile)
    snum=0
    for line in idata:
        bus_id=line[2]
        user_id=line[1]
        if(user_id not in rlist):
            if(int(line[3])>3):
                tlist=tlist+numpy.array(map(float,line[5:]))
                snum=snum+1
            elif(int(line[3])<3):
                tlist=tlist-numpy.array(map(float,line[5:]))
                snum=snum+1
        else:
            subnum=subnum+1
    if(snum>0):
        tlist=tlist/snum
    writer.writerow([bus_id]+list(tlist))
    ifile.close()
    snum=snum+1
    if(snum%1000==0):
        print snum
print "subnum",subnum
wfile.close()
