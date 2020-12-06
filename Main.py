from Tree import Tree

tree = Tree()

tree.insert(5)
tree.insert(10)
tree.insert(20)
tree.insert(25)
tree.insert(30)
tree.insert(35)
tree.insert(50)

tree.delete(25)
tree.delete(30)
tree.delete(35)

print("")
tree.showPre()
print("")
tree.showIn()
print("")
tree.showPos()
print("")
print("")

tree.draw()
