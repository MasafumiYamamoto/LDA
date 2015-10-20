import csv
import gensim

#file pass
pas=""
#prepare
dictionary=gensim.corpora.Dictionary.load(pas+"/nNV/nNVreview.dict")
corpus=gensim.corpora.MmCorpus(pas+"nNVreview.mm")
#use LSI
lsi=gensim.models.LsiModel.load(pas+"nNV/nNVreview.lsi")

wfile=open("topicword_LSI.csv","wb")
writer=csv.writer(wfile)
header=["Topic"]
for i in range(0,10):
    header.append("ww"+str(i).zfill(2))
    header.append("tw"+str(i).zfill(2))
writer.writerow(header)


for topic in range(0,lsi.num_topics):
    wlist=[]
    wlist.append(str(topic).zfill(2))
    word=lsi.print_topic(topic)
    word=word.replace("+"," ")
    word=word.replace("*"," ")
    wlist=wlist+word.split()
    writer.writerow(wlist)
wfile.close()
