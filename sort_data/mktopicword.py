import csv
import collections
import numpy

print "topic_num"
topic_num=raw_input()

vlist=collections.Counter()
vfile=open("C:/Users/masafumi/Desktop/Lresult/scmodoki100_5.csv","r")
vdata=csv.reader(vfile)
for line in vdata:
    vlist[str(line[0])]=numpy.array(line[1:])
print "vlist fin",len(vlist)
vfile.close()

wfile=open("LDA50topicword.csv","wb")
writer=csv.writer(wfile)
tlist=collections.Counter()
ifile=open("C:/Users/masafumi/Desktop/Lresult/LDAresult/train_nNV/topic_50/nNV_topicword_LDA.csv","r")
idata=csv.reader(ifile)
idata.next()
for line in idata:
    tlist[line[0]]=[0]*int(topic_num)
    vec=numpy.array([0]*int(topic_num))
    for t in range(0,int(topic_num)):
        print line[2*t+1]
        vec[t]=float(line[2*t+1])
    vec=vec/numpy.linalg.norm(vec)
    for t in range(0,int(topic_num)):
        tlist[line[0]]=tlist[line[0]]+vec[t]*vlist[str(2*t+1)]
#        tlist[line[0]]=tlist[line[0]]+float(line[2*t+1])*vlist[str(2*t+1)]
    writer.writerow([t]+list(tlist[line[0]]))
    print "line fin",line[0]
ifile.close()
wfile.close()
