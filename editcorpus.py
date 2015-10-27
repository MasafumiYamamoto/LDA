from gensim import corpora, models, similarities
import csv
import textedit
import time
pas="D:/Lresult/"

print "start",time.ctime()
dlist=[]
dfile=open(pas+"nNVreview.csv","r")
ddata=csv.reader(dfile)
dnum=0
for line in ddata:
	te=line[0]
	doc=textedit.textedit(te)
	dlist.append(doc)
	dnum=dnum+1
	if(dnum%100000==0):
		print dnum,
dfile.close()
#print dlist
print "dfile fin",time.ctime()
texts = [[word for word in document.lower().split()] for document in dlist]
print "text fin",len(dlist),time.ctime()

##dictionary_load
dictionary=corpora.Dictionary.load(pas+"/corpus_pl/nNVreviewpl.dict")

####stopword_load
sfile=open(pas+"stopwords/over4word.csv","r")
sdata=csv.reader(sfile)
slist=[]
for line in sdata:
	slist.append(line[0])
print "slist fin",len(slist),time.ctime()

####remove_stopwords
print "before",len(dictionary.token2id)
for t in slist:
	if(t in dictionary.token2id):
		del dictionary.token2id[t]
print "after",len(dictionary.token2id)

dictionary.save(pas+"nNVreviewover4.dict")
dictionary.save_as_text(pas+"nNVreviewover4_text.dict")

###mk_corpus
corpus=[dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(pas+"nNVreviewover4.mm", corpus)

print "mk_corpus fin",time.ctime()
