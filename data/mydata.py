import os
import pickle
import collections
import gensim
import json

dataPath = 'mydata/videoId'
vocab_counter = collections.Counter()

def get_article(file):
    file = dataPath + '/' + file
    d = open(file,'r',encoding='utf-8').read()
    tokens = list(gensim.utils.tokenize(d,lower=True))
    vocab_counter.update(tokens)
    article=[]
    count = 0
    temp = ''
    for t in tokens:
        if count<50:
            temp += t + ' '
            count += 1
        else:
            article += [temp]
            temp= ''
            count = 0
    article += [temp]
    return article

def get_abtract(file):
    file = dataPath + '/' + file + '.json'
    with open(file) as f:
        json_data = json.load(f)
    abstract = []
    for comments in json_data['comments'][:3]:
        abstract += [comments['textOriginal']]
    return abstract

i=0
for file in os.listdir(dataPath):
    if file.endswith(".txt"):
        dict = {}
        dict['id'] = file[:-4]
        dict['article']=get_article(file)
        dict['abstract']=get_abtract(dict['id'])
        filename = 'mydata/temp/'+str(i)+'.json'
        with open(filename,'w',encoding="utf-8") as f:
            json.dump(dict,f,indent="\t")
        i += 1

with open("mydata/vocab_cnt.pkl",'wb') as vocab_file:
    pickle.dump(vocab_counter, vocab_file)

with open("mydata/vocab_cnt.pkl",'rb') as f:
    pk = pickle.load(f)

print(pk)