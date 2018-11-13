# coding: utf-8
#!/usr/bin/python2
import argparse
import codecs
import lxml.etree as ET
import os
import regex
import sys
#from newdp import buildTestdata,delete,build16Traindata,data_processing


lcode = 'zh'

import jieba 
print ("jieba succesfuly loaded!")
    
max_corpus_size = 1000000000
stopword_filepath = "./data/stopwords.txt"
stopwords = []

def read_in_stopword():
    global stopwords#读入停用词
    file_obj = codecs.open(stopword_filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        line=line.strip('\r\n')
        if not line:
            break
        stopwords.append(line)
    file_obj.close()




def clean_text(text):
    global lcode
    
    # Common
    text = regex.sub("(?s){{.+?}}", "", text) # remove markup tags
    text = regex.sub("(?s){.+?}", "", text) # remove markup tags
 #   text = regex.sub("(?s)\[\[([^]]+\|)", "", text) # remove link target strings
    text = regex.sub("(?s)\[\[([^]]+\:.+?]])", "", text) # remove media links
    
    text = regex.sub("[']{5}", "", text) # remove italic+bold symbols
    text = regex.sub("[']{3}", "", text) # remove bold symbols
    text = regex.sub("[']{2}", "", text) # remove italic symbols
    

    text = regex.sub(u"[^\r\n\p{Han}。！？]", "", text)

    
    # Common
    text = regex.sub("[ ]{2,}", " ", text) # Squeeze spaces.
    return text

def sentence_segment(text):

    sents = regex.split(u"[\n]+", text) 
   
    return sents
        
def word_segment(sent,stop = True):

    global  stopwords
    words = list(jieba.cut(sent, cut_all=False)) 
    results = []

    for word in words:
        if word in stopwords and stop:
            continue#去除停用词
        results.append(word)
 
    return results

def build_corpus(filename,savename):
    global lcode, max_corpus_size, fname 
    read_in_stopword()   
    with codecs.open(savename.format(lcode), 'w', 'utf-8') as fout:
        i = 1
        j = 1
        #ns = "{http://www.mediawiki.org/xml/export-0.10/}" # namespace
        
        file_obj = codecs.open(filename,'r','utf-8')
        sentences = file_obj.readlines()
        for sentence in sentences:
            running_text = sentence.strip('\n').split(',')[0]
            try:
                running_text = clean_text(running_text)
                sents = sentence_segment(running_text)
                for sent in sents:
                    if sent is not None:
                        words = word_segment(sent)
                        if lcode in ['ja']:
                            fout.write(" ".join(words).decode('utf8') + "\n")
                        else:
                            fout.write(" ".join(words) + "\n")
                  
                                           
            except:
                continue # it's okay as we have a pretty big corpus!
            #elem.clear() # We need to save memory!
            if i % 1000 == 0: 
                print (i,end=""),
                fsize = os.path.getsize(filename.format(lcode))
               
            i += 1

 




if __name__ == "__main__":


    filename = './data/output.txt'
    savename = './data/weibo_nof_vec.txt'
    build_corpus(filename,savename)

    #delete()
    #build16Traindata()


 


    #build_answer('./data/answers.txt')

