#!/usr/bin/env python

int_max= 999999999999
int_min = -99999999999


class Node:

	def __init__(self,val):
		self.data = val
		self.left = None 
		self.right = None 


def isBST(node):

	return(isBSTUtil(node,int_min,int_max))

def isBSTUtil(node, mini, maxi):

	if node is None:
		return True
	if node.data <mini or node.data >maxi:
		return False
	return(isBSTUtil(node.left,mini,node.data-1)and isBSTUtil(node.right,node.data+1,maxi))



root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
 
if (isBST(root)):
    print "Is BST"
else:
    print "Not a BST"