#!/usr/bin/env python

def addList(a,b):

	r_a = a.reverse()
	r_b = b.reverse()
	final_list=[]

	if len(a) > len(b):
		for i in range(len(a) - len(b)):
			b.append(0)
	else:
		for i in range(len(b) - len(a)):
			a.append(0)


	temp_list=[0]


	for i in range(len(a)):
		temp = a[i] + b[i] + int(temp_list[0])

		if temp > 9:
			temp_list = [i for i in str(temp)]
			final_list.append(int(temp_list[1]))

		else:
			final_list.append(temp)
			temp_list=[0]

	final_list.reverse()
	print final_list

