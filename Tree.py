from Node import Node

class Tree():

    def __init__(self):
        self.root = None

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

    def delete(self, value):
        self.root = self.__deleteNode(self.root, value)

    def __deleteNode(self, aux, value):
        if value < aux.value:
            aux.left = self.__deleteNode(aux.left, value)
            if (self.getHeight(aux.left) - self.getHeight(aux.right)) == 2:
                if value < aux.left.value:
                    aux = self.simpleLeft(aux)
                else:
                    aux = self.doubleLeft(aux)

        elif value > aux.value:
            aux.right = self.__deleteNode(aux.right, value)
            if (self.getHeight(aux.right) - self.getHeight(aux.left)) == 2:
                if value > aux.right.value:
                    aux = self.simpleRight(aux)
                else:
                    aux = self.doubleRight(aux)

        else:
            if aux.left == None:
                return aux.right
            elif aux.right == None:
                return aux.left
            else:
                node = aux
                aux = self.getMin(node.right)
                aux.right = self.deleteMin(node.right)
                aux.left = node.left

        r = self.getHeight(aux.right)
        l = self.getHeight(aux.left)
        m = self.getMax(r, l)
        aux.height = m + 1

        return aux
    
    def getMin(self, aux):
        if  aux.left == None:
            return aux
        return self.getMin(aux.left)

    def deleteMin(self, aux):
        if  aux.left == None:
            return aux.right
        
        aux.left = self.deleteMin(aux.left)
        r = self.getHeight(aux.right)
        l = self.getHeight(aux.left)
        m = self.getMax(r, l)
        aux.height = m + 1

        return aux
