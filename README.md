# IE3320

both the py file can run directly.

 ---raw data---
## 1. build_corpus_.py:

* Cut words and clean data 
* line116: file path to process 
* line177: file path to save result

---cuted data---

## 2. LDA_.py:

* Devide the data into several \# of topics
* num_topics: \# of topics
* /data/topic_0~num_topics-1.txt: categorized weibo
* /data/topic_num_topics.txt: weibo which can't be categorized
* line16: open the file

--data in topics--

## 3. classify.py
Classify blogs

## 4. count.py
Count the distribution of classified blogs

## data:


### Tools
#### ntused-negative/positive.txt
dictionary for emotional key words
####stopwords.txt: 800+ stopwords.

### cutword
Files after data clean

### sentiment
file after sentiment classification

#### Result.txt
The result of the data classification. The order of the result is the same as the input file.
n represents negative
p represents positive
middle represents the number of negative and positive words are the same
cannot classify represents there are no key word in this blog

#### count_result.txt
The distribution of classification result

### Topic

#### topic_0 - 10.txt
The blogs for different topics.
