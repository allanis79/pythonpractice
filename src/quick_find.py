#!/usr/bin/env python

a = None

def array(n):
	global a

	a=[0]*n

	for i in range(n):

		a[i] = i

	return a

def connected(p,q):
	return a[p] == a[q]


def union(p,q):

	#print asu

	temp_1 = a[p]
	temp_2 = a[q]
	#print temp_1
	#print temp_2


	for i in range(len(a)):

		if a[i] == temp_1:
			#print a[i]
			a[i] = temp_2
			#print a[i]


	#print a



def quickfind():

	a = array(10)
	print a

	print connected(0,1)
	union(0,1)
	print connected(0,1)
	print connected(1,2)
	union(1,2)
	print connected(1,2)
	print a


quickfind()