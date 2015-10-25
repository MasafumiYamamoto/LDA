import csv
import glob

print "topic_num"
topic_num=raw_input()
print "LDA or LSI"
model=raw_input()

pas="C:/Users/masafumi/Desktop/Lresult/"+str(model)+"result/train_nNV/topic_"+str(topic_num)+"/business_"+str(model)
slist=glob.glob(pas+"/*")
wfile=open("hoge.csv","wb")
writer=csv.writer(wfile)
wlist=["rev_id","user_id","bus_id","rate","date"]

for num in range(0,int(topic_num)):
    wlist.append("t"+str(num).zfill(len(str(topic_num))))
writer.writerow(wlist)

for shop in slist:
    ifile=open(shop,"r")
    idata=csv.reader(ifile)
    for line in idata:
        writer.writerow(line)
    ifile.close()
wfile.close()
