from gensim import corpora, models, similarities
pas="D:/Lresult/over4/"

dictionary = corpora.Dictionary.load(pas+"nNV/nNVreivewover4.dict")
corpus = corpora.MmCorpus(pas+"nNV/nNVreivewover4.mm")

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a modl
corpus_tfidf=tfidf[corpus]
print "tfidf fin"

lsi=models.LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=500)
corpus_lsi=lsi[corpus_tfidf]
#print corpus_lsi
lsi.save(pas+"nNVreivewover4_t500.lsi")
