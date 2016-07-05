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


def Mirror(root):

	if root is None:
		return

	if root.left is None and root.right is  None:
		return


	root.left, root.right = root.right,root.left

	if root.left:
		Mirror(root.left)

	if root.right:
		Mirror(root.right)




root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

root.inorder()
Mirror(root)
print root.value
print root.left.value
print root.right.value
print root.right.left.value
print root.right.right.value



