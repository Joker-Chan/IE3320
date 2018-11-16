r = open('first_step.txt', 'r', encoding='utf-8')
neg_d = open('./dict/ntusd-negative.txt', 'r', encoding='utf-8')
pos_d = open('./dict/ntusd-positive.txt', 'r', encoding='utf-8')
w = open('result.txt', 'w')

neg_list = list()
pos_list = list()
line_number = 0

for line in neg_d:
	line = line.strip()
	neg_list.append(line)

for line in pos_d:
	line = line.strip()
	pos_list.append(line)

for line in r:
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
	elif n < p:
		new_line = 'p\n'
	elif n == 0:
		new_line = 'cannot classify\n'
	else:
		new_line = 'middle\n'

	w.write(new_line)

w.close()
r.close()
neg_d.close()
pos_d.close()