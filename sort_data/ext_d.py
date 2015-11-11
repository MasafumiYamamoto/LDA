def main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_):
    import csv
    import glob
    import numpy
    import collections
    import time

    tnum=int(tnum_)
    #path="D:/Lresult/"
    path=str(rootpath_)
    bnum=int(bnum_)
    model=str(model_)

    rfile=open(path+"subrev_1000.csv","r")
    rdata=csv.reader(rfile)
    rdata.next()
    rlist=collections.Counter()
    for line in rdata:
        rlist[line[0]]=1
    #print "rlist",len(rlist),time.ctime()
    wfile=open(path+"subrev_1000_"+model+"_o4b"+str(bnum)+"t"+str(tnum)+".csv","wb")
    writer=csv.writer(wfile)
    header=["rev_id","user_id","bus_id","rating","date"]
    for num in range(0,int(tnum)):
        header.append("t"+str(num).zfill(2))
    writer.writerow(header)
    slist=glob.glob(path+"b"+str(bnum)+"t"+str(tnum)+"_"+model+"_business/*")
    subnum=0
    revnum=0
    print "slist",len(slist),time.ctime()
    for shop in slist:
        wlist=[]
        tlist=numpy.array([0]*tnum)
        ifile=open(shop,"r")
        idata=csv.reader(ifile)
        for line in idata:
            revnum=revnum+1
            bus_id=line[2]
            rev_id=line[0]
            if(rev_id in rlist):
                subnum=subnum+1
                writer.writerow(line)
        ifile.close()
    print "subrev",revnum,subnum
    wfile.close()
    rfile.close()

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
    print "mdoel"
    model=raw_input()
    main(rootpath_,tnum_,bnum_,rflag_,tflag_,model_)
