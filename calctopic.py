pas=""

from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load(pas+"nNVreivew.dict")
corpus = corpora.MmCorpus(pas+"nNVreivew.mm")


#use LDA
lda = models.LdaModel.load(pas+"NVreview.lda")
doc = "Human computer interaction"

vec_bow = dictionary.doc2bow(doc.lower().split())
print vec_bow

vec_lda = lda[vec_bow]
print vec_lda
