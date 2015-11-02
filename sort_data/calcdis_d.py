def main(rootpath_,tnum_,bnum_,rflag_,tflag_):
	import time
	import csv
	import math
	import collections
	import glob
	import numpy
	import time
	import os

	pas=str(rootpath_)
	tnum=int(tnum_)
	bnum=int(bnum_)
	rflag=int(rflag_)

	ifile=open(pas+"subrev1000_LSI_b"+str(bnum)+"t"+str(tnum)+".csv","r")
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
	sfile=open("hoge.csv","wb")
	if(rflag!=1):
		sfile=open(pas+"mergeLSI_nrnt_b"+str(bnum)+"t"+str(tnum)+".csv","r")
	elif(rflag_==1):
		sfile=open(pas+"mergeLSI_rnt_b"+str(bnum)+"t"+str(tnum)+".csv","r")
	sdata=csv.reader(sfile)
	slist=collections.Counter()
	slen=collections.Counter()
	sdata.next()
	for line in sdata:
		slist[line[0]]=numpy.array(map(float,line[1:]))
		slen[line[0]]=numpy.linalg.norm(slist[line[0]])
	print "slen",len(slist),len(slist[line[0]])
	l=0
	if(rflag!=1):
		os.mkdir(pas+"resnrnt_b"+str(bnum)+"t"+str(tnum))
	elif(rflag==1):
		os.mkdir(pas+"resrnt_b"+str(bnum)+"t"+str(tnum))
	for line in ilist:
		l=l+1
		outfile=open(pas+"hoge.csv","wb")
		if(rflag!=1):
			outfile=open(pas+"resnrnt_b"+str(bnum)+"t"+str(tnum)+"/"+line+".csv","wb")
		elif(rflag==1):
			outfile=open(pas+"resrnt_b"+str(bnum)+"t"+str(tnum)+"/"+line+".csv","wb")
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

if __name__ == '__main__':
    print "csvfile"
    rootpath_=raw_input()
    print "tnum"
    tnum_=raw_input()
    print "bnum"
    bnum_=raw_input()
    print "rflag"
    rflag_=raw_input()
    print "tflag"
    tflag_=raw_input()
    main(rootpath_,tnum_,bnum_,rflag_,tflag_)
