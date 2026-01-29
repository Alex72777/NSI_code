from binarytree import Node, build

root = Node("racine")
root.left = Node("sag", Node("ssag"), Node("ssad"))
root.right = Node("sad")
print(root)

l = [1,
     2, 3,
     None, 5, 3, None]

a = build(l)
print(a)

def infixe(arbre: Node) -> list:
    if arbre == None:
        return []
    else:
        return infixe(arbre.left) + [arbre.value] + infixe(arbre.right)

def prefixe(arbre: Node) -> list:
    if arbre == None:
        return []
    else:
        return [arbre.value] + prefixe(arbre.left) + prefixe(arbre.right)

def postfixe(arbre: Node) -> list:
    if arbre == None:
        return []
    else:
        return postfixe(arbre.left) + postfixe(arbre.right) + [arbre.value]

# print(infixe(root))
# print(prefixe(root))
# print(postfixe(root))

assert infixe(root) == ['ssag', 'sag', 'ssad', 'racine', 'sad']
assert prefixe(root) == ['racine', 'sag', 'ssag', 'ssad', 'sad']
assert postfixe(root) == ['ssag', 'ssad', 'sag', 'sad', 'racine']