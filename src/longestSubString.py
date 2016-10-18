#!/usr/bin/env python

def LongestSubString(s):
	last = [-1] * 256

	i = maxlen = 0 


	for j in range(len(s)):

		if last[ord(s[j])] >=i:
			i = last[ord(s[j])] + 1


		last[ord(s[j])] = j 

		maxlen = max(maxlen,j-i+1)

	for i,j in enumerate(last):
		if j > 0:
			print chr(i),


	return maxlen 



z = LongestSubString('abba cdef!!!')
print z 