#!/usr/bin/env python



class Node:

	def __init__(self,val):
		self.value = val 
		self.left = None 
		self.right = None 

	def inorder(self):
		

		if self:
			if self.left:
				self.left.inorder()
			print self.value
			

			if self.right:
				self.right.inorder()


def findSum(root):

	if root == None:
		return 0

	old_value = root.value


	root.value = findSum(root.left) + findSum(root.right)

	return root.value + old_value


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

root.inorder()
findSum(root)
root.inorder()
