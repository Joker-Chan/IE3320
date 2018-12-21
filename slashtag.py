import pickle
import json
import codecs
def extracttopic(sentence):
	topic = ""
	seg = sentence.split('#')
	if(len(seg) > 2):
		topic = seg[1]
	if(topic in topic_dict):
		topic_dict[topic] += 1
	else:
		topic_dict[topic] = 1


if __name__ == '__main__':	
    topic_dict = dict()
    text = ""
    print("reading files")
    for i in range(1,11):
        path = './data/raw/output'+str(i)+'.txt'
        f = open(path)    
        for line in f.readlines():
        	extracttopic(line)            
        f.close()

    sorted_list = sorted(topic_dict.items(), key=lambda item:item[1], reverse=True)
    sorted_list = sorted_list[:2000]
    #print(sorted_list)
    #with codecs.open("./data/topics.txt",'w',encoding='') as f:
    f = open("./data/topics.txt","w")
    f.write(json.dumps(sorted_list,ensure_ascii=False))

    #print(topic_dict)