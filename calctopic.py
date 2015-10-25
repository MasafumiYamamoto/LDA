from gensim import corpora, models, similarities
import csv
import textedit
pas="

dictionary = corpora.Dictionary.load(pas+"NV/NVreview.dict")
corpus = corpora.MmCorpus(pas+"NV/NVreview.mm")


#use LDA
lda = models.LdaModel.load(pas+"NV/NVreview.lda")


#calc topic sim
header=[]
header.append("rev_id")
header.append("bus_id")
for num in range(1,51):
	header.append(str(num))

wfile=open("subrevtopic.csv","wb")
writer=csv.reader(wfile)
writer.writerow(header)

ifile=open("subrev.csv","r")
idata=csv.reader(ifile)
idata.next()
for line in idata:
	wlist=[]
	wlist.append(line[0])
	wlist.append(line[1])
	doc=textedit.textedit(line[2])
	vec_bow = dictionary.doc2bow(doc.lower().split())
	vec_lda = lda[vec_bow]
	slist=[0]*50
	for num in range(0,len(vec_lda)):
		slist[vec_lda[num][0]]=vec_lda[num][1]
	wlist=wlist+slist
	writer.writerow(wlist)

ifile.close()
wfile.close()
