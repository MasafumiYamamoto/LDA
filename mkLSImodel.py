from gensim import corpora, models, similarities
pas=""

dictionary = corpora.Dictionary.load(pas+"nNV/nNVreivew.dict")
corpus = corpora.MmCorpus(pas+"nNV/nNVreivew.mm")

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a modl
corpus_tfidf=tfidf[corpus]
print "tfidf fin"

lsi=models.LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=50)
corpus_lsi=lsi[corpus_tfidf]
#print corpus_lsi

lsi.save(pas+"nNV/nNVreivew.lsi")
