#for rev_shop

import csv
import glob

print "topicnum"
N=raw_input()

wfile=open("topic"+str(N)+".csv","wb")
wri=csv.writer(wfile)
wri.writerow(["revid","mybus","ranking","topscore","topbus","myscore"])
revlist=glob.glob("C:/Users/masafumi/Desktop/LDAresult/train_nNV/topic_200/res/*")
l=0
for review in revlist:
	ifile=open(review,"r")
	idata=csv.reader(ifile)
	idata.next()
	seikai=0
	top=-1
	tbus=""
	mybus=""
	revid=""
	for line in idata:
		if(line[1]==line[3]):
			seikai=float(line[2])
			mybus=line[3]
			revid=line[0]
		if(top<float(line[2])):
			top=float(line[2])
			tbus=line[1]
	ifile=open(review,"r")
	idata=csv.reader(ifile)
	idata.next()
	rank=1
	for line in idata:
		if(seikai<float(line[2])):
			rank=rank+1
	wri.writerow([revid,mybus,rank,top,tbus,seikai])
	l=l+1
	if(l%10==0):
		print l
	ifile.close()

wfile.close()
