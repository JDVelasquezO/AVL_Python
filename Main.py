from Tree import Tree

tree = Tree()

tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(5)
tree.insert(7)
tree.insert(10)

tree.delete(2)

print("")
tree.showPre()
print("")
tree.showIn()
print("")
tree.showPos()
print("")
print("")
