#!/usr/bin/env python


def conversion(fromNum,frombase,tobase):
	toNum = 0
	power = 0

	while fromNum > 0:
		toNum += frombase ** power *(fromNum%tobase)
		fromNum //= tobase
		power +=1


	return toNum



if __name__ == '__main__':
	r = conversion(101011,2,10)
	print r

