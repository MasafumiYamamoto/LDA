import csv
import glob
import numpy
import collections
import time

def main():
    print "busfile pass"
    spas="D:/Lresult/over4/b1t500_business"
    print "topicnum"
    topicnum=int(raw_input())
    path="D:/Lresult/"
    rfile=open(path+"subrev_1000.csv","r")
    rdata=csv.reader(rfile)
    rdata.next()
    rlist=collections.Counter()
    for line in rdata:
        rlist[line[0]]=1
    print "rlist",len(rlist),time.ctime()

    wfile=open(path+"subrev_1000_b1t"+str(topicnum)+".csv","wb")
    writer=csv.writer(wfile)
    header=["bus_id","user_id","bus_id","rating","date"]
    for num in range(0,int(topicnum)):
        header.append("t"+str(num).zfill(2))
    writer.writerow(header)
    slist=glob.glob(path+"over4/b1t"+str(topicnum)+"_business/*")
    subnum=0
    revnum=0
    print "slist",len(slist),time.ctime()
    for shop in slist:
        wlist=[]
        tlist=numpy.array([0]*topicnum)
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
    main()
