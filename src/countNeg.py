#!/usr/bin/env python 


def countNeg(M,n,m):

	count = 0 
	i = 0 
	j = m-1 

	while j >=0 and i < n: 

		if M[i][j] <0:

			count +=(j+1)
			i += 1 

		else:
			j -=1

	return count 


M = [ 
	[-3, -2, -1,-1, 1],
	[-2, -2, 3, 4],
	[-4, 5, 7, 8]
	]

print countNeg(M,3,4)