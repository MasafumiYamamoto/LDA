import csv
import gensim

#file pass
pas="D:/Lresult/s5/"
#prepare
dictionary=gensim.corpora.Dictionary.load(pas+"nNVreview.dict")
corpus=gensim.corpora.MmCorpus(pas+"nNVreview.mm")
#use LDA
lda=gensim.models.LsiModel.load("C:/Users/masafumi/Desktop/Lresult/LSIresult/train_nNV/topic_200/nNVreview200.lsi")

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
