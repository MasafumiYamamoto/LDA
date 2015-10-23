import csv
import collections
import time

path="C:\Users\masafumi\Desktop\LDAresult"
ifile=open(path+"/train_nNV/topic_200/nNVrevtopic200_LDA.csv","r")
idata=csv.reader(ifile)
idata.next()
rfile=open(path+"/NVreview.csv","r")
rdata=csv.reader(rfile)
rdata.next()
rlist=collections.Counter()
for line in rdata:
    rlist[line[0]]=[line[0],line[1],line[2],line[3],line[4]]

print len(rlist)
k=0
for line in idata:
    wfile=open(path+"/train_nNV/topic_200/business_LDA/"+line[1]+".csv","ab")
    writer=csv.writer(wfile)
    wlist=rlist[line[0]]
    wlist=wlist+line[2:]
    writer.writerow(wlist)
    k=k+1
    if(k%100000==0):
        print k,time.ctime()

ifile.close()
wfile.close()
