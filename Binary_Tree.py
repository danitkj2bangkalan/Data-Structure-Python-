#14 - Binary Tree
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, new_node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, new_node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
myt=BinaryTree("a")
print(myt.getRootVal)


"""
( = '+ note baru dari current dan jadikan noteini sebagai parrent note
operator = set nilai key dengan operator tersebut, tambahkan node baru dri current node dan jadikan right child ini sebagai current node, baru
operan = set nilai key dengan operan dan jadikan parent dri node tsb menjadi current node
) = kembali ke parentdari current node
"""
#stack  operator

def stack():
    s=[]
    return(s)
def push(s,data):
    s.append(data)
def pop(s):
    data=s.pop()
    return(data)
def peek(s):
    return (s[len(s)-1])
def IsEmpty(s):
    return (s==[])
def size(s):
    return len(s)

def buildParseTree(mathExp):
    tokenList = mathExp.split()
    parentStack = stack()
    expTree = BinaryTree(' ')
    push(parentStack,expTree)
    print(tokenList)
    currentTree = expTree
    for i in tokenList:
        if i == '(' :
            print('if 1', i)
            currentTree.insertLeft(' ' )
            push(parentStack,currentTree) 
            currentTree = currentTree.getLeftChild()
        elif i not in [ '+' , '-' , '*' , '/' , ')' ]:
            print('if 2', i)
            currentTree.setRootVal(int(i))
            parent = pop(parentStack)
            currentTree = parent
        elif i in [ '+' , '-' , '*' , '/' ]:
            print('if 3', i) 
            currentTree.setRootVal(i)
            currentTree.insertRight(' ')
            push(parentStack,currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')' :
            currentTree = pop(parentStack)
        else:
            raise ValueError
    return expTree
import operator

    def evaluate(parsetree):
        opers = { '+' :operator.add, '-' :operator.sub, '*' :operator.mul,'/' :operator.truediv}
        left = parsetree.getLeftChild()
        right = parsetree.getRightChild()
        if left and right:
            fn = opers[parsetree.key]
            return fn(evaluate(left),evaluate(right))
        else:
            return parse_tree.key

print(buildParseTree('( 3 + ( 4 * 5 ) )'))

#evaluasi  matematika menggunakan recursive