"""
Séparer une pile de nombre entiers en deux piles de nombres pairs et impairs
"""

from piles import Stack

def sort(pile: Stack):
	odd_stack = Stack()
	even_stack = Stack()

	while not pile.is_empty():
		value = pile.pop()
		if value % 2:
			odd_stack.push(value)
		else:
			even_stack.push(value)

	return odd_stack, even_stack

if __name__ == "__main__":
	pile = Stack()
	for i in range(1, 7):
		pile.push(i)
	odd_stack, even_stack = sort(pile)
	print("Odd Stack", odd_stack)
	print("Even Stack", even_stack)
