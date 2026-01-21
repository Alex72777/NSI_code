from exo_5p104 import Stack
"""
Inverser les éléments d'une pile
"""

class Queue:
	def __init__(self):
		self._data = []
	
	def enqueue(self, value: object):
		self._data.append(value)
	
	def dequeue(self) -> object:
		if self.is_empty():
			raise RuntimeError("Empty Queue")
		return self._data.pop(0)
	
	def is_empty(self) -> bool:
		if not self._data:
			return True
		return False


def reverse(pile: Stack):
	print(pile)
	tampon = Queue()
	while not pile.is_empty():
		value = pile.pop()
		tampon.enqueue(value)
	
	while not tampon.is_empty():
		value = tampon.dequeue()
		pile.push(value)
	
	print(pile)

pile = Stack()
for i in range(1, 6):
	pile.push(i)
reverse(pile)
