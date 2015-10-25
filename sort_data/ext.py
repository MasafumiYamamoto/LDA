import csv
import glob
import numpy
import collections

print "busfile pass"
spas="C:/Users/masafumi/Desktop/Lresult/LSIresult/train_nNV/topic_50/business_LSI"
print "topicnum"
topicnum=int(raw_input())

rfile=open("subrev_1000.csv","r")
rdata=csv.reader(rfile)
rdata.next()
rlist=collections.Counter()
for line in rdata:
    rlist[line[0]]=1
print "rlist",len(rlist)

wfile=open("subrev_1000_topic"+str(topicnum)+".csv","wb")
writer=csv.writer(wfile)
header=["bus_id","user_id","bus_id","rating","date"]
for num in range(0,int(topicnum)):
    header.append("t"+str(num).zfill(2))
writer.writerow(header)
slist=glob.glob(spas+"/*")
subnum=0
revnum=0
print "slist",len(slist)
for shop in slist:
    wlist=[]
    tlist=numpy.array([0]*topicnum)
    ifile=open(shop,"r")
    idata=csv.reader(ifile)
    for line in idata:
        revnum=revnum+1
        bus_id=line[2]
        rev_id=line[0]
        if(rev_id in rlist):
            subnum=subnum+1
            writer.writerow(line)
    ifile.close()
print "subrev",revnum,subnum
wfile.close()
