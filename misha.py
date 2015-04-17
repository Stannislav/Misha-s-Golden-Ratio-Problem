import matplotlib.pyplot as plt
import numpy as np


lim = 10
res = [[i+1,0,0] for i in xrange(lim)]
res[0][1] = 1
res[0][2] = 2


def print_res():
	for row in res:
		print "{}\t{}\t{}".format(row[0], row[1], row[2])

def can_find(number, max_row):
	for row in res:
		if number == row[1] or number == row[2]:
			return True
	return False

def fill_res():
	for row in res[1:]:
		candidate = row[0]+1
		while can_find(candidate, row[0]):
			candidate += 1
		row[1] = candidate
		row[2] = row[0] + row[1]

def plot_res():
	title = "{} rows".format(lim)
	filename = "{}_rows".format(lim)
	trans_res = map(list, zip(*res))
	m2, c2 = np.polyfit(trans_res[0], trans_res[1],1)
	m3, c3 = np.polyfit(trans_res[0], trans_res[2],1)
	print "Second column: {0:8.7f}x + {1:8.7f}".format(m2,c2)
	print "Third column: {0:8.7f}x + {1:8.7f}".format(m3,c3)
	print "m2/m1 = {0:8.7f}".format(m3*1.0/m2)
	xp = np.array(trans_res[0])

	plt.title(title)
	plt.plot(xp, trans_res[0], label='1 column')
	plt.plot(xp, trans_res[1], label='2 column')
	plt.plot(xp, trans_res[2], label='3 column')
	plt.plot(xp, m2*xp+c2, 'c--', label='2 column linear fit')
	plt.plot(xp, m3*xp+c3, 'm--', label='3 column linear fit')
	plt.legend(loc='upper left')
	plt.savefig(filename)
	plt.show()

fill_res()
print_res()
plot_res()
