import csv
import collections
import numpy

print "topic_num"
topic_num=raw_input()

vlist=collections.Counter()
vword=collections.Counter()
vlen=collections.Counter()
vfile=open("C:/Users/masafumi/Desktop/Lresult/scmodoki100_5.csv","r")
vdata=csv.reader(vfile)
tw=0
for line in vdata:
    vword[tw]=str(line[0])
    vlist[tw]=numpy.array(map(float,line[1:]))
    #print type(vlist[tw])
    vlen[tw]=numpy.linalg.norm(vlist[tw])
    tw=tw+1
print "vlist fin",tw
vfile.close()

wfile=open("LDA50topicword.csv","wb")
writer=csv.writer(wfile)
writer.writerow(["topic","1","2","3","4","5"])
tlist=collections.Counter()
ifile=open("LDA50topicvec.csv","r")
idata=csv.reader(ifile)
for line in idata:
    base=numpy.array(map(float,line[1:]))
    baselen=numpy.linalg.norm(base)
    sim=collections.Counter()
    top=-100
    topt=-1
    for t in range(0,len(vlist)):
        if(baselen!=0 and vlen[t]!=0):
            sim[t]=numpy.dot(base,vlist[t])/baselen/vlen[t]
            if(top<sim[t]):
                top=sim[t]
                topt=t
    writer.writerow([line[0],top,vword[topt]])
ifile.close()
wfile.close()
