from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load("C:\Users\masafumi\Desktop\LDA/nNVreivew.dict")
corpus = corpora.MmCorpus("C:\Users\masafumi\Desktop\LDA/nNVreivew.mm")

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a modl
corpus_tfidf=tfidf[corpus]

lda=models.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=3)
corpus_lda=lda[corpus_tfidf]
print lda
#print corpus_lda

lda.save("C:\Users\masafumi\Desktop\LDA/nNVreivew.lda")

