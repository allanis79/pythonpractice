#!/usr/bin/env python

z=[]
class Node(object):

	def __init__(self,val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
		


	def insert(self,data):

		if self. value == data:
			return False
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True


	def find(self,data):

		if self.value == data:
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False

		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False

	def preorder(self):

		if self:
			print str(self.value)
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		

		if self:
			if self.leftChild:
				self.leftChild.postorder()

			if self.rightChild:
				self.rightChild.postorder()

			print str(self.value)


	def inorder(self):
		global z 
		

		if self:
			if self.leftChild:
				self.leftChild.inorder()
			z.append(self.value)
			

			if self.rightChild:
				self.rightChild.inorder()

		return z 



		

		

class Tree(object):

	def __init__(self):
		self.root = None


	def insert(self, data):
		if self.root:
			return self.root.insert(data)

		else:
			self.root = Node(data)
			return True


	def find(self,data):

		if self.root:
			return self.root.find(data)

		else:
			return False


	

	def remove(self,data):

		#empty tree

		if self.root is None:
			return False

		# data is in root node
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild

			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild

				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild

				self.root.value = delNode.value

				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild

				else:

					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None

					else:
						delNodeParent.rightChild = None

			return True


		parent = None

		node = self.root


		#find node to remove

		while node and node.value != data:
			parent = node

			if data < node.value:
				node = node.leftChild
			elif data > node. value:
				node = node.rightChild

		# 1 data not found

		if node is None or node.value != data:
			return False

		# 2 remove node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None

			else:
				parent.rightChild = None

			return True


		#3 remove node had left child only

		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild

			else:
				parent.rightChild = node.rightChild

		#4 remove node had only right child

		elif node.leftChild is None and node.rightChild:

			if data < parent.value:
				parent.leftChild = node.leftChild

			else:
				parent.rightChild = node.rightChild

		#5 remove node has both childs

		else:

			delNodeParent = node

			delNode = node.rightChild

			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild

			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None






	def preorder(self):

		if self.root is not None:

			print 'preorder........'

			self.root.preorder()


	def postorder(self):

		if self.root is not None:
			print 'postorder.......'


			self.root.postorder()



	def inorder(self):

		if self.root is not None:
			print 'inorder.......'

			l = self.root.inorder()
			print l
			res=all(l[i]<l[i+1] for i in xrange(len(l)-1))
			if res:
				print 'is bst'
			else:
				print 'not bst'

		
			
			



if __name__ == '__main__':

	bst = Tree()

	print bst.insert(10)
	print bst.insert(100)
	print bst.insert(120)
	print bst.insert(19)
	print bst.insert(5)
	#print bst.remove(19)
	print bst.remove(56)

	bst.preorder()
	bst.postorder()

	bst.inorder()
	


