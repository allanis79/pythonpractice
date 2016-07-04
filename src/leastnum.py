#!/usr/bin/env python


def leastnum(n):

	lst =[i for i in str(n) ]

	temp_lst = [] 

	
	
	for i in range(len(lst)):
		lst = [num for num in str(n) ]
		lst.pop(i)
		#temp_lst.append(map(lambda i:int(i),lst))
		temp_lst.append(lst)

	temp_nums = [int(''.join(i)) for i in temp_lst]

	mini = min(temp_nums)
	return mini 


def main(n,k):
	final = n 

	for i in range(k):
		z = leastnum(final)
		final = z

		


	print final 



		
main(1234,2)