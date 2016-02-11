#!/usr/bin/env python


#usage: ./gcf num1 num2

import sys


def gcf(num1,num2):
	num1 = int(num1)
	num2 = int(num2)
	if num1 > num2:
		num1,num2 = num2,num1

	for x in range(num1,0,-1):
		if num1%x ==0 and num2%x ==0:
			return x




if __name__ == '__main__':


	GCF = gcf(sys.argv[1],sys.argv[2])
	print GCF
