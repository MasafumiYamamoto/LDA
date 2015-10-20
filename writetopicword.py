import csv
import gensim

#file pass
pas=""
#prepare
dictionary=gensim.corpora.Dictionary.load(pas+"/nNV/nNVreview.dict")
corpus=gensim.corpora.MmCorpus(pas+"nNVreview.mm")
#use LDA
lda=gensim.models.LdaModel.load(pas+"nNV/nNVreview.lda")

wfile=open("topicword.csv","wb")
writer=csv.writer(wfile)
header=["Topic"]
for i in range(0,10):
    header.append("ww"+str(i).zfill(2))
    header.append("tw"+str(i).zfill(2))
writer.writerow(header)

for topic in range(0,lda.num_topics):
    wlist=[]
    wlist.append(str(topic).zfill(2))
    word=lda.print_topic(topic)
    word=word.replace("+"," ")
    word=word.replace("*"," ")
    wlist=wlist+word.split()
    writer.writerow(wlist)
wfile.close()
