def main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_):
    import csv
    import glob
    import numpy
    import collections
    import time

    path=rootpath_
    tnum=int(tnum_)
    bnum=int(bnum_)
    rflag=int(rflag_)
    tflag=int(tflag_)
    model=str(model_)

    rfile=open(path+"subrev_1000.csv","r")
    rdata=csv.reader(rfile)
    rdata.next()
    rlist=collections.Counter()
    for line in rdata:
        rlist[line[0]]=1
    #print "rlist",len(rlist)
    wfile=open(path+"hoge.csv","wb")
    if(rflag!=1):
        wfile=open(path+"merge"+model+"_nrnt_b"+str(bnum)+"t"+str(tnum)+".csv","wb")
    elif(rflag==1):
        wfile=open(path+"merge"+model+"_rnt_b"+str(bnum)+"t"+str(tnum)+".csv","wb")
    writer=csv.writer(wfile)
    header=["bus_id"]
    for num in range(0,int(tnum)):
        header.append("t"+str(num).zfill(tnum/10))
    writer.writerow(header)
    slist=glob.glob(path+"b"+str(bnum)+"t"+str(tnum)+"_"+model+"_business/*")
    subnum=0
    revnum=0
    print "slist",len(slist)
    for shop in slist:
        wlist=[]
        tlist=numpy.array([0]*int(tnum))
        ifile=open(shop,"r")
        idata=csv.reader(ifile)
        snum=0
        for line in idata:
            revnum=revnum+1
            bus_id=line[2]
            rev_id=line[0]
            if(rev_id not in rlist):
                if(int(rflag)!=1):
                    tlist=tlist+numpy.array(map(float,line[5:5+int(tnum)]))
                    snum=snum+1
                    subnum=subnum+1
                elif(int(rflag)==1):
                    if(int(line[3])>3):
                        tlist=tlist+numpy.array(map(float,line[5:5+int(tnum)]))
                    elif(int(line[3])<3):
                        tlist=tlist-numpy.array(map(float,line[5:5+int(tnum)]))
                    snum=snum+1
                else:
                    print "rflag miss"
            else:
                subnum=subnum+1
        if(snum>0):
            tlist=tlist/snum
        writer.writerow([bus_id]+list(tlist))
        ifile.close()
        snum=snum+1
        if(revnum%1000==0):
            print revnum,time.ctime()
    print "subnum",subnum
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
    print "model"
    model_=raw_input()
    main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_)
