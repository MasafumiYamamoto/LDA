#for each review calc simirality

import time
import csv
import math
import collections
import glob
import numpy
pas="D:/Lresult/"
print "topicnum"
topicnum=raw_input()

ifile=open(pas+"over4/subrev_1000_b1t"+str(topicnum)+"_LSI.csv","r")
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
sfile=open(pas+"over4/mergeLSI_nrnt_over4b1t"+str(topicnum)+".csv","r")
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
	outfile=open(pas+"over4/resb1t500nrnt/"+line+".csv","wb")
	outwriter=csv.writer(outfile)
	outwriter.writerow(["revid","shop","sim","seikai"])
	for shop in slist:
		score=0
		if(ilen[line]!=0 and slen[shop]!=0):
			score=numpy.dot(ilist[line],slist[shop])/ilen[line]/slen[shop]
			outwriter.writerow([line,shop,score,iseikai[line]])
	if(l%100==0):
		print l
outfile.close()
ifile.close()
sfile.close()
