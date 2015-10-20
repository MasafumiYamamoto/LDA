import csv
import glob
import numpy

print "file pass"
spas=raw_input()
print "topicnum"
topicnum=int(raw_input())

wfile=open("mergeLDA"+str(topicnum)+".csv","wb")
writer=csv.writer(wfile)
header=["bus_id"]
for num in range(0,int(topicnum)):
    header.append("t"+str(num).zfill(2))
writer.writerow(header)
slist=glob.glob(spas+"/*")
snum=0
for shop in slist:
    wlist=[]
    tlist=numpy.array([0]*topicnum)
    ifile=open(shop,"r")
    idata=csv.reader(ifile)
    for line in idata:
        bus_id=line[2]
        tlist=tlist+numpy.array(map(float,line[5:]))
    writer.writerow([bus_id]+list(tlist))
    ifile.close()
    snum=snum+1
    if(snum%1000==0):
        print snum
wfile.close()
