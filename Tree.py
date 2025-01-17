from Node import Node
from graphviz import Digraph

class Tree():

    def __init__(self):
        self.root = None
        self.i = 59
        self.dot = Digraph(comment='AVL Tree')

    def getHeight(self, aux):
        if aux == None:
            return -1
        else:
            return aux.height

    def getMax(self, r, l):
        return (l, r)[r>l]

    def insert(self, value):
        self.root = self.__insertNode(self.root, value)

    def __insertNode(self, aux, value):

        if aux == None:
            aux = Node(value)
            self.aplhabet = list(map(chr, range(self.i, 127)))
            aux.name = self.aplhabet[0]
            self.i += 1
            self.dot.node(f"{aux.name}", f"{aux.value}")

        elif (value < aux.value):
            aux.left = self.__insertNode(aux.left, value)

            if (self.getHeight(aux.left) - self.getHeight(aux.right)) == 2:
                if value < aux.left.value:
                    aux = self.simpleLeft(aux)
                else:
                    aux = self.doubleLeft(aux)

        elif (value > aux.value):
            aux.right = self.__insertNode(aux.right, value)
        
            if (self.getHeight(aux.right) - self.getHeight(aux.left)) == 2:
                if value > aux.right.value:
                    aux = self.simpleRight(aux)
                else:
                    aux = self.doubleRight(aux)
        else:
            raise

        r = self.getHeight(aux.right)
        l = self.getHeight(aux.left)
        m = self.getMax(r, l)
        aux.height = m + 1
        return aux

    def doubleLeft(self, aux):
        aux.left = self.simpleRight(aux.left)
        return self.simpleLeft(aux)

    def doubleRight(self, aux):
        aux.right = self.simpleLeft(aux.right)
        return self.simpleRight(aux)

    def simpleLeft(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        node.height = self.getMax(self.getHeight(node.left), self.getHeight(node.right)) + 1
        left.height = self.getMax(self.getHeight(left.left), node.height)+1
        return left

    def simpleRight(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        node.height = self.getMax(self.getHeight(node.left), self.getHeight(node.right)) + 1
        right.height = self.getMax(self.getHeight(right.left), node.height) + 1
        return right

    def showIn(self):
        self.__showInOrder(self.root)

    def showPos(self):
        self.__showPosOrder(self.root)

    def showPre(self):
        self.__showPreOrder(self.root)

    def __showInOrder(self, aux):
        if aux != None:
            self.__showInOrder(aux.left)
            print(f"{aux.value} ", end="")
            self.__showInOrder(aux.right)

    def __showPosOrder(self, aux):
        if aux != None:
            self.__showPosOrder(aux.left)
            self.__showPosOrder(aux.right)
            print(f"{aux.value} ", end="")

    def __showPreOrder(self, aux):
        if aux != None:
            print(f"{aux.value} ", end="")
            self.__showPreOrder(aux.left)
            self.__showPreOrder(aux.right)

    def balancedTree(self, node):
        if self.balanceFactor(node) > 1:
            if self.balanceFactor(node.right) < 0:
                node.right = self.simpleLeft(node.right)
            node = self.simpleRight(node)
        elif self.balanceFactor(node) < -1:
            if self.balanceFactor(node.left) > 0:
                node.left = self.simpleRight(node.left)
            node = self.simpleLeft(node)
        return node

    def balanceFactor(self, node):
        return self.getHeight(node.right) - self.getHeight(node.left)

    def delete(self, value):
        self.root = self.__deleteNode(self.root, value)

    def __deleteNode(self, aux, value):
        if value < aux.value:
            aux.left = self.__deleteNode(aux.left, value)

        elif value > aux.value:
            aux.right = self.__deleteNode(aux.right, value)

        else:
            if aux.left == None:
                return aux.right
            elif aux.right == None:
                return aux.left
            else:
                node = aux
                aux = self.getNodeMin(node.left)
                aux.right = self.replaceNodeLeft(node.left)
                aux.left = node.left

        r = self.getHeight(aux.right)
        l = self.getHeight(aux.left)
        m = self.getMax(r, l)
        aux.height = m + 1
        return self.balancedTree(aux)
    
    def getNodeMin(self, aux):
        if  aux.right == None:
            return aux
        return self.getNodeMin(aux.right)

    def replaceNodeLeft(self, aux):
        if  aux.right == None:
            return aux.left
        
        aux.left = self.replaceNodeLeft(aux.left)
        r = self.getHeight(aux.right)
        l = self.getHeight(aux.left)
        m = self.getMax(r, l)
        aux.height = m + 1
        return self.balancedTree(aux)

    def draw(self):
        self.__drawNode(self.root)
        self.dot.render('test-output/avl_tree.png', view=True)

    def __drawNode(self, node):
        if (node != None):
            
            root = f"{node.name}"

            if node.left == None:
                childRight = f"{node.right.name}"
                self.dot.edges([root+childRight])

                if node.right.right != None:
                    self.__drawNode(node.right)

                if node.right.left != None:
                    self.__drawNode(node.right)

            elif node.right == None:
                childLeft = f"{node.left.name}"
                self.dot.edges([root+childLeft])
                
                if node.left.left != None:
                    self.__drawNode(node.left)

                if node.left.right != None:
                    self.__drawNode(node.left)

            else:
                childLeft = f"{node.left.name}"
                childRight = f"{node.right.name}"
                self.dot.edges([root+childLeft, root+childRight])
                
                if node.right.right != None or node.right.left != None:
                    self.__drawNode(node.right)

                if node.left.right != None or node.left.left != None:
                    self.__drawNode(node.left)
