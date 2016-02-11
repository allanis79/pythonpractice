#!/usr/bin/env python

def lcm(*args):

	a = sorted(args)
	#print type(a[0])
	mul=1
	for i in range(len(a)):
		mul *=a[i]

	print mul
	print a[-1]


	for x in range(a[-1],mul+1,a[-1]):
		if x%a[0] == 0:
			return x




if __name__ == '__main__':
	r = lcm(6,9,27)
	print r