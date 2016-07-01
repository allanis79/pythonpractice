#!/usr/bin/env python

class node:

	def __init__(self,val):
		self.value = val 
		self.left = None 
		self.right = None


	def insert(self,data):

		if self.value == data:
			return False
		elif self.value > data:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = node(data)
				return True
		else:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = node(data)
				return True



class tree:

	def __init__(self,root):
		self.root = None 


	def insert(self,data):

		if self.root:
			return self.root.insert(data)
		else:
			self.root = node(data)
			return True


	def findmindepth(self,root):

		if self.root == None:
			return 0 

		if self.root.left == None and self.root.right == None:
			return 1 

		if self.root.left == None:

			return findminheight(self.root.right)+1 

		if self.root.right == None:

			return findminheight(self.root.left) + 1


		return min(findminheight(self.root.left),findminheight(self.root.right))+1
