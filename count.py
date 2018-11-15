r = open('result.txt', 'r')
w = open('count_result.txt', 'w')

n = 0
p = 0
c = 0
m = 0
t = 0

for line in r:
	if line[0] == 'n':
		n += 1
	elif line[0] == 'p':
		p += 1
	elif line[0] == 'c':
		c += 1
	elif line[0] == 'm':
		m += 1

	t += 1

w.write('negative:' + str(float(n)/float(t)) + '\n')
w.write('positive:' + str(float(p)/float(t)) + '\n')
w.write('cannot:' + str(float(c)/float(t)) + '\n')
w.write('middle:' + str(float(m)/float(t)) + '\n')