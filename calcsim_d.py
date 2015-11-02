def main(model_,bnum_,tnum_,train_,pas_):
	from gensim import corpora, models, similarities
	import csv
	import textedit
	import time
	model=str(model_)
	bnum=int(bnum_)
	tnum=int(tnum_)
	train=str(train_)
	pas=str(pas_)

	print "start",time.ctime()

	dictionary = corpora.Dictionary.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".dict")
    corpus = corpora.MmCorpus(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".mm")

	#use LSI
	lsi = models.LsiModel.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".lsi")
	if(model=="lda"):
		lsi=models.LdaModel.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".lda")

	#calc topic sim
	header=[]
	header.append("rev_id")
	header.append("bus_id")
	for num in range(0,int(topic_num)):
		header.append("t"+str(num).zfill(int(tnum)/10))

	wfile=open(pas+train+model+"_o4b"+str(bnum)+"t"+str(tnum)+".csv","wb")
	writer=csv.writer(wfile)
	writer.writerow(header)

	"NVreview.csv:[review_id,user_id,business_id,stars,date,texts]"
	ifile=open(pas+train+".csv","r")
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

if __name__ == '__main__':
	print "model"
	model_=raw_input()
	print "bnum"
	bnum_=raw_input()
	print "tnum"
	tnum_=raw_input()
	print "train"
	train_=raw_input()
	print "pas"
	pas_=raw_input()
	main(model_,bnum_,tnum_,train_,pas_)
