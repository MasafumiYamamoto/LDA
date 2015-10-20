import csv
import collections
import time

ifile=open("train_nNV/nNVrevtopic_LDA.csv","r")
idata=csv.reader(ifile)
idata.next()
rfile=open("NVreview.csv","r")
rdata=csv.reader(rfile)
rdata.next()
rlist=collections.Counter()
for line in rdata:
    rlist[line[0]]=[line[0],line[1],line[2],line[3],line[4]]

print len(rlist)
k=0
for line in idata:
    wfile=open("train_nNV/business_LDA/"+line[1]+".csv","ab")
    writer=csv.writer(wfile)
    wlist=rlist[line[0]]
    wlist=wlist+line[2:]
    writer.writerow(wlist)
    k=k+1
    if(k%100000==0):
        print k,time.ctime()

ifile.close()
wfile.close()
