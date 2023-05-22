class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root):
        self.root = root
        
    def sums(self, node):
        total = node.value
        for child in node.children:
            total += self.sums(child)
        return total

    def sibling(self, node):
        if node.parent is None:
            return 0
        total = 0
        for sibling in node.parent.children:
            total += sibling.value
        return total

root = Node(200)
a = Node(23, root)
b = Node(11, root)
c = Node(13, a)
d = Node(57, a)
e = Node(32, b)
f = Node(42, c)
g = Node(51, c)
h = Node(71, c)
i = Node(12, d)
j = Node(15, d)
k = Node(33, e)
l = Node(8, e)

root.add_child(a)
root.add_child(b)
a.add_child(c)
a.add_child(d)
b.add_child(e)
c.add_child(f)
c.add_child(g)
c.add_child(h)
d.add_child(i)
d.add_child(j)
e.add_child(k)
e.add_child(l)

tree = Tree(root)

total_sum = tree.sums(root)
print(f"Total value of Node {root.value} and all of its descendants = {total_sum}")

sibling_sum = tree.sibling(k)
print(f"Total value of all siblings of Node {k.value} = {sibling_sum}")
