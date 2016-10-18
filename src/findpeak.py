#!/usr/bin/env python


def findPeak(alist):

	for i in range(len(alist)-2):

		if alist[i+2]<alist[i+1] > alist[i]:
			print 'found peak',alist[i+1]


findPeak([4,67,12,4,2,45,54])