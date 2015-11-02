def main(rootpath_,tnum_,bnum_,rflag_,tflag_):
	import csv
	import glob

	N=int(tnum_)
	rflag=int(rflag_)
	pas=str(rootpath_)
	rflag=int(rflag_)
	tflag=int(tflag_)
	bnum=int(bnum_)

	wfile=open(pas+"hoge.csv","ab")
	if(rflag!=1):
		wfile=open(pas+"ranking_nrntb"+str(bnum)+"t"+str(N)+".csv","wb")
	elif(rflag==1):
		wfile=open(pas+"ranking_rntb"+str(bnum)+"t"+str(N)+".csv","wb")
	wri=csv.writer(wfile)
	wri.writerow(["revid","mybus","ranking","topscore","topbus","myscore"])
	revlist=[]
	if(rflag!=1):
		revlist=glob.glob(pas+"resnrnt_b"+str(bnum)+"t"+str(N)+"/*")
	elif(rflag==1):
		revlist=glob.glob(pas+"resrnt_b"+str(bnum)+"t"+str(N)+"/*")
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
		if(l%100==0):
			print l
		ifile.close()
	wfile.close()

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
