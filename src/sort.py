#!/usr/bin/env python


def insertion_sort(A):
	for i in range(1,len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1,-2,-1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]


			else:
				break

		A[k+1] = curNum



	return A



def selection_sort(A):
	for i in range(0,len(A)-1):
		minIndex = i
		for j in range(i+1,len(A)):
			if A[j] < A[minIndex]:
				minIndex = j

		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]
		

	return A

def bubbleSort(A):
	for i in range(0,len(A)-1):
		for j in range(0,len(A)-1-i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]



	return A

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
    return alist




def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)

	return A
	
def quick_sort2(A, low, hi):
	if low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)
	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	pivot = hi
	if low < mid:
		if mid < hi:
			pivot = mid
	elif low < hi:
		pivot = low
	
	return pivot
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)

l =[4,3,9,7,87,65,89,44,54]

print quick_sort(l)

