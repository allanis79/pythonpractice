#!/usr/bin/env python

class Node(object):

	def __init__(self,d,n =None):
		self.data =d
		self.next = n



class linkedlist():

	def __init__(self,r=None):
		self.root = r 
		self.size = 0


	def push(self,d):
		new_node = Node(d,self.root)
		self.root = new_node
		self.size +=1

	def detectloop(self):
		slow = self.root 
		fast = self.root 

		while slow and fast and fast.next:
			slow = slow.next 
			fast = fast.next.next 

			if slow == fast: 
				print True 
				return
		else:
			print False 
			return


# Driver program for testing
llist = linkedlist()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
 
# Create a loop for testing
llist.root.next.next.next = llist.root
llist.detectloop()
		