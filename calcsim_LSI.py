from gensim import corpora, models, similarities
import csv
import textedit
pas=""

dictionary = corpora.Dictionary.load(pas+"nNV/nNVreview.dict")
corpus = corpora.MmCorpus(pas+"nNV/nNVreview.mm")

#use LSI
lsi = models.LsiModel.load(pas+"nNV/nNVreview.lsi")


#calc topic sim
header=[]
header.append("rev_id")
header.append("bus_id")
for num in range(1,51):
header.append("t"+str(num))

wfile=open("nNVrevtopic_LSI.csv","wb")
writer=csv.writer(wfile)
writer.writerow(header)

#NVreview:[review_id,user_id,bus_id,stars,date,text]
ifile=open("NVreview.csv","r")
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
