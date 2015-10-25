from gensim import corpora, models, similarities
import csv
import textedit
pas="C:\Users\masafumi\Desktop\Lresult/"

dictionary = corpora.Dictionary.load(pas+"nNVreview.dict")
corpus = corpora.MmCorpus(pas+"nNVreview.mm")

#use LSI
lsi = models.LsiModel.load(pas+"LSIresult/train_nNV/topic_200/nNVreview200.lsi")

#calc topic sim
header=[]
header.append("rev_id")
header.append("bus_id")
for num in range(1,201):
	header.append("t"+str(num))

wfile=open("nNVrevtopic_LSI_200.csv","wb")
writer=csv.writer(wfile)
writer.writerow(header)

#NVreview:[review_id,user_id,bus_id,stars,date,text]
ifile=open(pas+"NVreview.csv","r")
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
slist=[0]*50
for num in range(0,len(vec_lda)):
	slist[vec_lsi[num][0]]=vec_lsi[num][1]
wlist=wlist+slist
writer.writerow(wlist)

ifile.close()
wfile.close()
