from gensim import corpora, models, similarities
import csv
import textedit
pas=""

# remove common words and tokenize
stopfile=open("stopwords_en.csv","r")
stopdata=csv.reader(stopfile)
stoplist=[]
for line in stopdata:
	stoplist.append(line[0])
stopfile.close()
#print stoplist

##make documents
dlist=[]
#dfile=open("notNVreview.csv","r")
dfile=open("testrev.csv")
ddata=csv.reader(dfile)
for line in ddata:
	te=line[0]
	doc=textedit.textedit(te)
	dlist.append(doc)
dfile.close()
#print dlist

texts = [[word for word in document.lower().split() if word not in stoplist] for document in dlist]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

print(texts)
print("texts fin")

dictionary = corpora.Dictionary(texts)
#dictionary.save('/deerwester.dict') # store the dictionary, for future reference
dictionary.save_as_text(pas+"nNVreivew.dict")

corpus=[dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(pas+"nNVreivew.mm", corpus)