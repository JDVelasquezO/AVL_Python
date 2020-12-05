from Node import Node

class Tree():

    def __init__(self):
        self.root = None

    def getHeight(self, aux):
        if aux == None:
            return -1
        else:
            return aux.height

    def maxi(self, r, l):
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
                    aux = self.srl(aux)
                else:
                    aux = self.drl(aux)

        elif (value > aux.value):
            aux.right = self.__insertNode(aux.right, value)
            if (self.getHeight(aux.right) - self.getHeight(aux.left)) == 2:
                if value > aux.right.value:
                    aux = self.srr(aux)
                else:
                    aux = self.drr(aux)
        else:
            raise

        r = self.getHeight(aux.right)
        l = self.getHeight(aux.left)
        m = self.maxi(r, l)
        aux.height = m + 1
    
        return aux

    def drl(self, aux):
        aux.left = self.srr(aux.left)
        return self.srl(aux)
    
    def drr(self, aux):
        aux.right = self.srl(aux.right)
        return self.srr(aux)

    def srl(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        node.height = self.maxi(self.getHeight(node.left), self.getHeight(node.right)) + 1
        left.height = self.maxi(self.getHeight(left.left), node.height)+1
        return left

    def srr(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        node.height = self.maxi(self.getHeight(node.left), self.getHeight(node.right)) + 1
        right.height = self.maxi(self.getHeight(right.left), node.height) + 1
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