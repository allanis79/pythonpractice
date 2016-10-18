#!/usr/bin/env python

def binary_search(data,target,low,high):

	mid = int(data[low]+dat[high])/2
	mid_value = data[mid]
	if low > high:
		return False 
	elif  target == mid_value:
		return True
	elif target < mid_value:
		high = mid 
		binary_search(data,target,low,high-1)
	elif target > mid_value:
		low = mid 
		binary_search(data,target,low+1,high)
