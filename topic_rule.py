import numpy as np
import re
f = open("./data/cutword/weibo_nof_vec.txt", "r", encoding='utf-8')
origin = f
lines = f.readlines()
origins = lines
job = open("./data/topic/job.txt",'w')
love = open("./data/topic/love.txt",'w')
study = open("./data/topic/study.txt",'w')
health = open("./data/topic/health.txt",'w')
family = open("./data/topic/family.txt",'w')
count = np.zeros(5)
for i in range(0,len(lines)):
	sentence = lines[i]
	origin_sen = origins[i]
	if re.search('工作|老板|入职|辞职|工资|薪水|同事', sentence):
		job.write(origin_sen)
		count[0] += 1
		
	if re.search('女朋友|男朋友|老公|老婆|爱人|女票|男票',sentence):
		love.write(origin_sen)
		count[1]+= 1
	if re.search('作业|成绩|学校|学习|考试|高中|大学|论文', sentence):
		study.write(origin_sen)
		count[2]+= 1
	if re.search('生病|头疼|疼|健康|养生|猝死|累|去世', sentence):
		health.write(origin_sen)
		count[3]+= 1
	if re.search('爸妈|父母|儿子|女儿|亲戚|妈妈|爷爷|奶奶',sentence):
		family.write(origin_sen)
		count[4]+= 1
	

job.close()
love.close()
study.close()
health.close()
family.close()

for k in range(5):
	print(count[k])
