class Stack:
	def __init__(self):
		self._data = []
	
	def push(self, value: object):
		self._data.append(value)
	
	def pop(self) -> object:
		if self.is_empty():
			raise RuntimeError("Empty Stack")
		value = self._data[-1]
		self._data = self._data[:-1]
		return value
	
	def is_empty(self) -> bool:
		if not self._data:
			return True
		return False
	
	def __str__(self):
		return str(self._data)

def main():
	p = Stack()
	p.push(10)
	p.push(11)
	p.push(12)
	p.push(13)
	v = p.pop()
	print(p)
	print(p.is_empty())
	for i in range(3):
		p.pop()
	print(p.is_empty())

if __name__ == "__main__":
	main()
