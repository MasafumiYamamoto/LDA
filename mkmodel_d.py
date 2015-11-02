def main(model_,bnum_,tnum_,train_,pas_):
    from gensim import corpora, models, similarities
    import time
    model=str(model_)
	bnum=int(bnum_)
	tnum=int(tnum_)
	train=str(train_)
	pas=str(pas_)

    dictionary = corpora.Dictionary.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".dict")
    corpus = corpora.MmCorpus(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".mm")
    tfidf = models.TfidfModel(corpus) # step 1 -- initialize a modl
    corpus_tfidf=tfidf[corpus]
    print "tfidf fin",time.ctime()

    if(model=="lsi"):
        lsi=models.LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=tnum)
        corpus_lsi=lsi[corpus_tfidf]
        lsi.save(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".lsi")
    if(model=="lda"):
        lda=models.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=tnum)
        corpus_lda=lda[corpus_tfidf]
        lda.save(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".lda")

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
