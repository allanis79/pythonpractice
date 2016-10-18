#!/usr/bin/env python


class node:

	def __init__(self,val):

		self.value = val 
		self.left = None 
		self.right = None


def findPath(root,path,k):

	if root == None:
		return False 

	path.append(root.value)

	if root.value == k:
		return True

	if root.left != None and findPath(root.left,path,k) or root.right != None and findPath(root.right,path,k):
		return True 

	path.pop()
	return False 


def findLCA(root,n1,n2):

	if root == None:
		return False

	path1=[]
	path2=[]

	if not findPath(root,path1,n1) or not  findPath(root,path2,n2):
		return -1 

	while i <len(path1) and i <len(path2):

		if path1[i] != path2[i]:
			break 

		i +=1

	return path1[i-1]