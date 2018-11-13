# IE3320

both the py file can run directly.

---raw data---
1. build_corpus_.py:

Cut words and clean data
line116: file path to process
line177: file path to save result

---cuted data---
2. LDA_.py:
Devide the data into several \# of topics

num_topics: \# of topics
/data/topic_0~num_topics-1.txt: categorized weibo
/data/topic_num_topics.txt: weibo which can't be categorized
line16: open the file

--data in topics--

others:
data:
stopwords.txt: 800+ stopwords.
