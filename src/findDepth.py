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
				self.left.insert(data)
			else:
				self.left = node(data)
				return True

		else:
			if self.right:
				self.right.insert(data)
			else:
				self.right = node(data)
				return True




class tree:

	def  __init__(self):
		self.root = None 


	def insert(self,data):
		if self.root:
			self.root.insert(data)
		else:
			self.root  = node(data)
			return True



	def findmaxdepth(self,root):

		if self.root == None:
			return 0 
		else:
			ldepth = findmaxdepth(self.root.left)
			rdepth = findmaxdepth(self.root.right)


			if ldepth > rdepth:
				return ldepth+1

			else:
				return rdepth+1
