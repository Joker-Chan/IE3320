
import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')

from gensim.test.utils import common_texts, datapath
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel

from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
import os

import numpy as np
import matplotlib.pyplot as plt


f = open("./data/weibo_nof_vec.txt", "r", encoding='utf-8')
texts = [document.split() for document in f]

dictionary = Dictionary(texts)

dictionary.filter_extremes(no_above = 0.2)


corpus = [dictionary.doc2bow(text) for text in texts]

print('done with corpus.')

lda = LdaModel(corpus, id2word=dictionary, iterations=100, num_topics=10)

#print(lda.print_topics())
for i in range(0,10):
    print("-----------------------------------")
    print(lda.print_topic(i))

#lda.save('lda')
topic = []

for i in range (0,10):
    topic.append(open("./data/topic_" + str(i)+".txt", "w", encoding='utf-8'))
    topic[i].write(lda.print_topic(i) + '\n')
topic.append(open("./data/topic_10.txt", "w", encoding='utf-8'))
topic[10].write("empty topic" + '\n')
#print(dictionary[corpus[1][0][0]] + '-------------')


flag = False

origin = open("./data/output.txt").readlines()
for i in range(0,len(origin)):
    for index, score in sorted(lda[corpus[i]], key=lambda tup: -1*tup[1]):
        if score > 0.85:
            #print(corpus[i])
            #topic[index].write( dictionary[j[0]] for j in i)
            #for j in range(0, len(corpus[i])):
                #topic[index].write(dictionary[corpus[i][j][0]] + ' ')
            topic[index].write(origin[i] + ' ')
            #topic[index].write('\n')
            flag = True

        if (index == 9):
            if (flag == False):
                topic[10].write(origin[i] + ' ')
                #for j in range(0, len(corpus[i])):
                 #   topic[10].write(dictionary[corpus[i][j][0]] + ' ')
                #topic[10].write('\n')
            flag = False



        #print ("Score: {}\t Topic: {}".format(score, lda.print_topic(index, 10)))
    #print("-----------------------------------------------------------")
#print(corpus_lda)
