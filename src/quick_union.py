#!/usr/bin/env python

def array(n):
	global a

	a =[0] *n

	for i in range(n):

		a[i] = i


	return a


def connected(p,q):

	return root(p) == root(q)


def root(p):

	while p != a[p]:
		p = a[p]

	return p


def union(p,q):

	temp_i = root(p)
	temp_j = root(q)

	a[temp_i] = temp_j


def main():

	a = array(10)
	#print a

	#print connected(3,4)
	union(4,3)
	
	union(2,5)
	union(4,5)
	print connected(2,5)
	print connected(2,5)
	print connected(4,3)
	print connected(4,5)
	print connected(3,4)
	print connected(5,4)

	#print connected(4,5)
	print a


main()