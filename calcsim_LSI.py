from gensim import corpora, models, similarities
import csv
import textedit
import time

print "start",time.ctime()
pas="D:/Lresult/over4/"
print "topic_num"
topic_num=raw_input()

dictionary = corpora.Dictionary.load(pas+"corpus/nNVrev_o4b6.dict")
corpus = corpora.MmCorpus(pas+"corpus/nNVrev_o4b6.mm")

#use LSI
lsi = models.LsiModel.load(pas+"model/nNVrevo4b6_t"+str(topic_num)+".lsi")

#calc topic sim
header=[]
header.append("rev_id")
header.append("bus_id")
for num in range(0,int(topic_num)):
	header.append("t"+str(num).zfill(int(topic_num)/10))

wfile=open(pas+"nNVrev_LSI_t"+str(topic_num)+".csv","wb")
writer=csv.writer(wfile)
writer.writerow(header)

"NVreview.csv:[review_id,user_id,business_id,stars,date,texts]"
ifile=open("D:/Lresult/NVreview.csv","r")
idata=csv.reader(ifile)
idata.next()
k=0
for line in idata:
	wlist=[]
	wlist.append(line[0])
	wlist.append(line[2])
	doc=textedit.textedit(line[5])
	vec_bow = dictionary.doc2bow(doc.lower().split())
	vec_lsi = lsi[vec_bow]
        ###
	slist=[0]*int(topic_num)
	for num in range(0,len(vec_lsi)):
		slist[vec_lsi[num][0]]=vec_lsi[num][1]
	wlist=wlist+slist
	writer.writerow(wlist)
        k=k+1
	if(k%1000==0):
		print k,time.ctime()

ifile.close()
wfile.close()
print "fin",time.ctime()
