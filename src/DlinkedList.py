#!/usr/bin/env python

class Node(object):

	def __init__(self,d,n = None,p = None):
		self.data = d
		self.next_node = n
		self.prev_node = p


	def get_next(self):
		return self.next_node

	def set_next(self,n):
		self.next_node = n

	def get_prev(self):
		return self.prev_node

	def set_prev(self,p):
		self.prev_node = p 



	def get_data(self):
		return self.data

	def set_data(self,d):
		self.data = d




class LinkedList(object):

	def __init__(self,r = None):
		self.root = r
		self.size = 0



	def get_size(self):
		return self.size

	def Add(self,d):
		new_node = Node(d,self.root)
		if self.root:
			self.root.set_prev(new_node)
		self.root = new_node
		self.size +=1

	def remove(self,d):
		this_node = self.root
		prev_node = None

		while this_node:
			if this_node.get_data() == d:
				nex = this_node.get_next()
				prev = this_node.get_prev()

				if nex:
					nex.set_prev(prev)

				if prev:
					prev.set_next(nex)
				else:
					self.root = this_node
				self.size -=1
				return True

			else:
				this_node = this_node.get_next()
		return False


	def find(self,d):

		this_node = self.root
		while this_node:
			if this_node.get_data() == d:
				return d
			else:
				this_node = this_node.get_next()

		return None


if __name__ == '__main__':
	myList = LinkedList()
	myList.Add(5)
	myList.Add(9)
	myList.Add(1)
	myList.remove(1)
	print myList.remove(3)
	print myList.remove(5)
	print myList.find(9)




















