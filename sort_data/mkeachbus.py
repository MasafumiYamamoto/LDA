import csv
import collections
import time

print "topic_num"
topic_num=raw_input()

path="C:/Users/masafumi/Desktop/Lresult/"
ifile=open(path+"LSIresult/train_nNV/topic_"+str(topic_num)+"/nNVrevtopic"+str(topic_num)+"_LSI.csv","r")
idata=csv.reader(ifile)
idata.next()
rfile=open(path+"NVreview.csv","r")
rdata=csv.reader(rfile)
rdata.next()
rlist=collections.Counter()
for line in rdata:
    rlist[line[0]]=[line[0],line[1],line[2],line[3],line[4]]

print len(rlist),time.ctime()
k=0
for line in idata:
    wfile=open(path+"LSIresult/train_nNV/topic_"+str(topic_num)+"/business_LSI/"+line[1]+".csv","ab")
    writer=csv.writer(wfile)
    wlist=rlist[line[0]]
    wlist=wlist+line[2:]
    writer.writerow(wlist)
    k=k+1
    if(k%100000==0):
        print k,time.ctime()

ifile.close()
wfile.close()
