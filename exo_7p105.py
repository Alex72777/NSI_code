"""
Copier les élements d'une pile vers une autre pile
"""

from exo_5p104 import Stack

def copy(pile: Stack) -> Stack:
	print(pile)
	tampon = Stack()
	copied_stack = Stack()
	while not pile.is_empty():
		tampon.push(pile.pop())
	
	while not tampon.is_empty():
		copied_stack.push(tampon.pop())
	
	return copied_stack

if __name__ == "__main__":
	pile = Stack()
	for i in range(5):
		pile.push(i)
	copied_stack = copy(pile)
	print(copied_stack)
