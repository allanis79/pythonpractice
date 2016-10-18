#!/usr/bin/env python

def checkBrackets(text):
	a=[]
	opens=['[','{','(']
	closes=[']','}',')']
	alist = dict(zip(opens,closes))

	for i in text:

		if i in opens:
			a.append(i)
		if i in closes:
			if i != alist[a[-1]]:
				return 0 
			a.pop()

	if not a:
		return 1

	return 0 