import csv
import collections
import numpy

print "topic_num"
topic_num=raw_input()

vlist=collections.Counter()
vfile=open("C:/Users/masafumi/Desktop/Lresult/scmodoki100_5.csv","r")
vdata=csv.reader(vfile)
for line in vdata:
    vlist[str(line[0])]=numpy.array(map(float,line[1:]))
print "vlist fin"
vfile.close()

wfile=open("LDA50topicword.csv","wb")
writer=csv.writer(wfile)
tlist=collections.Counter()
ifile=open("C:/Users/masafumi/Desktop/Lresult/LDAresult/train_nNV/topic_50/nNV_topicword_LDA.csv","r")
idata=csv.reader(ifile)
idata.next()
for line in idata:
    tlist=[0]*100
    vec=[0]*10
    for t in range(0,10):
        vec[t]=float(line[2*t+1])
    vec=vec/numpy.linalg.norm(vec)
    for t in range(0,10):
        tlist=tlist+vec[t]*vlist[str(line[2*t+2])]
#        tlist[line[0]]=tlist[line[0]]+float(line[2*t+1])*vlist[str(2*t+1)]
    writer.writerow([line[0]]+list(tlist))
ifile.close()
wfile.close()
