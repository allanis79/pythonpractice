#!/usr/bin/env python

class node:

	def __init__(self,val):

		self.value = val
		self.left = None 
		self.right = None 




class tree:

	def __init__(self):
		self.root = None 



	def isBalanced(self,root):
		return isBalancedint(root) >=0

	def isBalancedint(self,root):
		if self.root == None:
			return 0 

		left = isBalancedint(self.root.left)
		right = isBalancedint(self.root.right)

		if left <0 or right < 0 or abs(left - right) > 1: 
			return -1 

		return max(left,right) + 1 