from Tree import Tree

tree = Tree()

tree.insert(5)
tree.insert(100)
tree.insert(41)
tree.insert(13)
tree.insert(15)
tree.insert(67)
tree.insert(46)
tree.insert(11)
tree.insert(55)
tree.insert(21)
tree.insert(29)
tree.insert(83)
tree.insert(71)
tree.insert(22)
tree.insert(3)

# tree.delete(25)
# tree.delete(30)
# tree.delete(35)

print("")
tree.showPre()
print("")
tree.showIn()
print("")
tree.showPos()
print("")
print("")

tree.draw()
