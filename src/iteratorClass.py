#!/usr/bin/env python 

class SequenceIterator:

	def __init__(self,sequence):

		self._seq = sequence
		self._k = -1 

	def __next__(self):

		self._l +=1
		if self._k <= len(self._seq):

			return self._seq[self._k]
		else:

			return StopIteration()

	def __iter__(self):

		return self

