import numpy as np
rs  = []
topics = ['job','love','study','health','family']
for i in range(5):
 rs.append(open('./data/topic/'+topics[i]+'.txt', 'r', encoding='utf-8'))


topicfiles = []
for i in range(5):
	topicfile = []
	topicfile.append(open('./data/sentiment/sheep/'+topics[i]+'_neg.txt', 'w+'))
	topicfile.append(open('./data/sentiment/sheep/'+topics[i]+'_pos.txt', 'w+'))
	topicfiles.append(topicfile)
#print(topicfiles)
neg_d = open('./data/tools/ntusd-negative.txt', 'r', encoding='utf-8')
pos_d = open('./data/tools/ntusd-positive.txt', 'r', encoding='utf-8')
w = open('./data/sentiment/sheep/result.txt', 'w+')

neg_list = list()
pos_list = list()
line_number = 0

for line in neg_d:
	line = line.strip()
	neg_list.append(line)

for line in pos_d:
	line = line.strip()
	pos_list.append(line)

p_count = np.zeros(5)
n_count = np.zeros(5)

for i in range(5):
	r = rs[i]
	for line in r:
		if '张艺兴' not in line:
			continue
		line_number += 1
		if line_number % 100 == 0:
			print(line_number)
		n = 0
		p = 0
		line = line.strip()
		words = line.split(' ')
		for word in words:
			if word in neg_list:
				n += 1
			if word in pos_list:
				p += 1

		if n > p:
			new_line = 'n\n'
			n_count[i] += 1
			#print(topicfiles[i][0])
			topicfiles[i][0].write(line+'\n')
		elif n < p:
			new_line = 'p\n'
			p_count[i] += 1
			topicfiles[i][1].write(line+'\n')
		elif n == 0:
			new_line = 'cannot classify\n'
		else:
			new_line = 'middle\n'
		#w.write(new_line)


r.close()
neg_d.close()
pos_d.close()

for i in range(5):
	total = float(n_count[i]+p_count[i])
	pos = p_count[i]/ total
	neg = n_count[i] / total
	st1 = "-------in topic \""+topics[i]+"\":------\n"
	st2 = "neg: " + str(neg) + " |||| pos: "+str(pos)+"\n\n"
	print(st1)
	print(st2)
	w.write(st1)
	w.write(st2)
w.close()
