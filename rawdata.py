#!/usr/bin/python3

import json
import os.path

readOut = open('./weibo.json','r', encoding='utf-8')
fp = open('./data/raw/output1.txt', 'a', encoding='utf-8')
index = 0
# content {"_id":{"$oid":"5a6c0687ac7eef81e560e923"},"reposts_num2":"321","reposts_num1":"0","level1":"普通用户","level2":"普通用户","zan_num2":"153","zan_num1":"2","is_repost":"1","phone2":"微博 weibo.com","address1":"","address2":"","phone1":"皮皮时光机","name2":"疯狂轻松背单词","name1":"经典丶古诗词","content1":"收藏学习~[鼓掌]","content2":"脱口而出100句经典口语！~[赞]","comments_num1":"0","comments_num2":"22"}
for line in readOut:
        if (index == 200000):
                fp.close()
                fp = open('./data/raw/output2.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 400000):
                fp.close()
                fp = open('./data/raw/output3.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 600000):
                fp.close()
                fp = open('./data/raw/output4.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 800000):
                fp.close()
                fp = open('./data/raw/output5.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 1000000):
                fp.close()
                fp = open('./data/raw/output6.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 1200000):
                fp.close()
                fp = open('./data/raw/output7.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 1400000):
                fp.close()
                fp = open('./data/raw/output8.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 1600000):
                fp.close()
                fp = open('./data/raw/output9.txt', 'a', encoding='utf-8')
                print('output done')
        if (index == 1800000):
                fp.close()
                fp = open('./data/raw/output10.txt', 'a', encoding='utf-8')
                print('output done')
        if (index > 2000000):
                break
        if line.startswith(u'\ufeff'):
                line = line.encode('utf8')[3:].decode('utf8')
        #print(line)
        pythonobj = json.loads(line)
        #print(pythonobj)
        #print(pythonobj.keys())
        pcontent1=pythonobj['content1']
        #print(pcontent1)
        pcontent2=pythonobj['content2']
        #print(pcontent2)
        fp.write(pcontent1+', '+pcontent2)
        fp.write('\n')
        index = index + 1
fp.close()

