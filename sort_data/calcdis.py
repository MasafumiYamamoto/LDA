#for each review calc simirality

import time
import csv
import math
import collections
import glob
import numpy

ifile=open("C:/Users/masafumi/Desktop/LDAresult/train_nNV/topic_50/subrev_1000_topic50.csv","r")
idata=csv.reader(ifile)
ilist=collections.Counter()
ilen=collections.Counter()
iseikai=collections.Counter()
irate=collections.Counter()
idata.next()
for line in idata:
	ilist[line[0]]=numpy.array(map(float,line[5:]))
	ilen[line[0]]=numpy.linalg.norm(ilist[line[0]])
	iseikai[line[0]]=line[2]
	irate[line[0]]=line[3]
print "list",len(ilist),len(ilist[line[0]])
#print ilen

sfile=open("C:/Users/masafumi/Desktop/LDAresult/train_nNV/topic_50/mergeLDA_rnt50_subrev.csv","r")
sdata=csv.reader(sfile)
slist=collections.Counter()
slen=collections.Counter()
sdata.next()
for line in sdata:
	slist[line[0]]=numpy.array(map(float,line[1:]))
	slen[line[0]]=numpy.linalg.norm(slist[line[0]])
print "slen",len(slist),len(slist[line[0]])
#print slen

l=0
for line in ilist:
	l=l+1
	for shop in slist:
		score=0
		if(ilen[line]!=0 and slen[shop]!=0):
			score=numpy.dot(ilist[line],slist[shop])/ilen[line]/slen[shop]
			if(int(irate[line])>3):
				#score=score*(-1)
				outfile=open("res5/"+line+".csv","wb")
				outwriter=csv.writer(outfile)
				outwriter.writerow(["revid","shop","sim","seikai"])
				outwriter.writerow([line,shop,score,iseikai[line]])
	if(l%100==0):
		print l
outfile.close()
ifile.close()
sfile.close()
