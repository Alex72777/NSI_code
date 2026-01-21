"""
Exercice 5 p 104
"""

class Stack:
    def __init__(self) -> None:
        self._data = []
    
    def push(self, v: object) -> None:
        self._data.append(v)
    
    def pop(self) -> object:
        if not self._data:
            raise RuntimeError("Empty Stack")
        val = self._data.pop()
        return val
    
    def is_empty(self) -> bool:
        if self._data:
            return False
        return True
    
    def __str__(self) -> str:
        return ", ".join([str(v) for v in self._data])

class Queue:
    def __init__(self) -> None:
        self._data = []
    
    def enqueue(self, v: object) -> None:
        self._data.append(v)
    
    def dequeue(self) -> object:
        if not self._data:
            raise RuntimeError("Empty Queue")
        val = self._data.pop(0)
        return val
    
    def is_empty(self) -> bool:
        if self._data:
            return False
        return True
    
    def __str__(self) -> str:
        return ", ".join([str(v) for v in self._data])

# p = Stack()
# p.push(10)
# p.push(11)
# p.push(12)
# p.push(13)
# v = p.pop()
# print(p)
# print(p.is_empty())
# [p.pop() for i in range(3)]
# print(p.is_empty())

"""
Exercice 6 p 104
"""

def reverse(p: Stack) -> None:
    f_tampon = Queue()
    while not p.is_empty():
        f_tampon.enqueue(p.pop())
    
    while not f_tampon.is_empty():
        p.push(f_tampon.dequeue())
    
    print(p)

# p = Stack()
# p.push(10)
# p.push(11)
# p.push(12)
# p.push(13)
# reverse(p)

"""
Exercice 7 p 105
"""

def copie(p: Stack) -> Stack:
    copie = Stack()
    vraicopie = Stack()
    while not p.is_empty():
        copie.push(p.pop())
    
    while not copie.is_empty():
        val = copie.pop()
        vraicopie.push(val)
        p.push(val)
    
    return vraicopie

# p = Stack()
# p.push(10)
# p.push(11)
# p.push(12)
# p.push(13)
# p_copy = copie(p)
# print(p_copy, p)

"""
Exercice 8 p 105
"""

def split(p: Stack):
    tampon = Stack()
    pairs = Stack()
    impairs = Stack()
    
    while not p.is_empty():
        tampon.push(p.pop())
    
    while not tampon.is_empty():
        val = tampon.pop()
        if val % 2:
            impairs.push(val)
        else:
            pairs.push(val)
        p.push(val)
    
    return pairs, impairs

# p = Stack()
# p.push(10)
# p.push(11)
# p.push(12)
# p.push(13)
# pairs, impairs = split(p)
# print("Pairs:", pairs, "Impairs:", impairs)

"""
Exercice 8 p 105
"""

def verifier_parenthesage(chars: str) -> None:
    tampon = Stack()
    
    for c in chars:
        if c == "(":
            tampon.push(1)
        elif c == ")":
            tampon.pop()

verifier_parenthesage("(()())")
verifier_parenthesage("(()")
verifier_parenthesage("())()(")