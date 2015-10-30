def main(rootpath_,tnum_,bnum_,rflag_,tflag_,infile_):
    import csv
    import collections
    import time
    import os

    tnum=int(tnum_)
    inputfile=str(infile_)
    path=str(rootpath_)
    bnum=int(bnum_)

    ifile=open(path+inputfile,"r")
    idata=csv.reader(ifile)
    idata.next()
    rfile=open("D:/Lresult/NVreview.csv","r")
    rdata=csv.reader(rfile)
    rdata.next()
    rlist=collections.Counter()
    for line in rdata:
        rlist[line[0]]=[line[0],line[1],line[2],line[3],line[4]]
    #print len(rlist),time.ctime()
    k=0
    os.mkdir(path+"b"+str(bnum)+"t"+str(tnum)+"_business")
    for line in idata:
        wfile=open(path+"b"+str(bnum)+"t"+str(tnum)+"_business/"+line[1]+".csv","ab")
        writer=csv.writer(wfile)
        wlist=rlist[line[0]]
        wlist=wlist+line[2:]
        writer.writerow(wlist)
        k=k+1
        if(k%100000==0):
            print k,time.ctime()
    ifile.close()
    wfile.close()

if __name__ == '__main__':
    print "csvfile"
    rootpath_=raw_input()
    print "topicnum"
    tnum_=raw_input()
    print "bnum"
    bnum_=raw_input()
    print "rflag"
    rflag_=raw_input()
    print "tflag"
    tflag_=raw_input()
    print "infile name"
    infile_=raw_input()
    main(rootpath_,tnum_,bnum_,rflag_,tflag_)
