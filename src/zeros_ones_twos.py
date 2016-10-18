#!/usr/bin/env python

dictonary ={}


def find(alist):

	for i in xrange(len(alist)):

		if alist[i] not in dictonary.keys():
			dictonary[alist[i]] = 1

		else:
			dictonary[alist[i]] +=1
	output =[]
	
	for i in dictonary.keys():
		temp = [i]*dictonary[i]
		output.extend(temp)

	print output




Input = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]


find(Input)