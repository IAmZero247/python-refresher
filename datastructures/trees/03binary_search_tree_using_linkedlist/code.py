import queue

class BSTNode:

    def __init__(self, data, left: 'BTNode' = None, right: 'BTNode' = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self, level=0):
        startwith = " " if level == 0 else "--"
        ret = (startwith * level) + '> ' + str(self.data) + "\n"
        if (self.left is not None):
            ret += self.left.__str__(level + 1)
        if (self.right is not None):
            ret += self.right.__str__(level + 1)
        return ret


#Insert
def insertBstNode(rootNode, nodeValue):
    if nodeValue is None:
        return None
    if rootNode is None:
        rootNode = BSTNode(nodeValue)
        return 'Inserted Succesfully'
    if (rootNode and rootNode.data is None):
        rootNode.data = nodeValue
        return 'Inserted Successfully'
    if rootNode.data >= nodeValue: # ->left
        if rootNode.left is None:
            rootNode.left = BSTNode(nodeValue)
            return 'Inserted Successfully'
        else:
            insertBstNode(rootNode.left, nodeValue)
    else : #rootNode.data < nodeValue  ->right
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
            return 'Inserted Successfully'
        else:
            insertBstNode(rootNode.right, nodeValue)
    return 'Failed To Insert'

#Traversal

def preOrderTraversal(rootNode:BSTNode):
    if not rootNode:
        return ''
    print(rootNode.data , '> ', end='')
    if rootNode.left is not None:
       preOrderTraversal(rootNode.left)
    if rootNode.right is not None:
       preOrderTraversal(rootNode.right)
    return None

def inOrderTraversal(rootNode:BSTNode):
    if not rootNode:
        return ''
    if rootNode.left is not None:
        inOrderTraversal(rootNode.left)
    print(rootNode.data, '> ', end='')
    if rootNode.right is not None:
        inOrderTraversal(rootNode.right)
    return None

def postOrderTraversal(rootNode:BSTNode):
    if not rootNode:
        return ''
    if rootNode.left is not None:
        postOrderTraversal(rootNode.left)
    if rootNode.right is not None:
        postOrderTraversal(rootNode.right)
    print(rootNode.data, '> ', end='')
    return None

def levelOrderTraversal(rootNode:BSTNode):
    if not rootNode:
        return ''
    qu = queue.Queue()
    qu.enqueue(rootNode)
    while(not qu.isEmpty()):
        element = qu.dequeue()
        print(element.value.data, '> ', end='')
        if element.value.left is not None:
            qu.enqueue(element.value.left)
        if element.value.right is not None:
            qu.enqueue(element.value.right)
bt1 = BSTNode(None)
print(bt1)
insertBstNode(bt1, 100)
insertBstNode(bt1, 200)
insertBstNode(bt1, 70)
insertBstNode(bt1, 300)
insertBstNode(bt1, 50)
insertBstNode(bt1, 400)
insertBstNode(bt1, 500)
insertBstNode(bt1, 25)
insertBstNode(bt1, 10)
insertBstNode(bt1, 5)
insertBstNode(bt1, 1)
print(bt1)

bt2 = BSTNode(None)
print(bt2)
insertBstNode(bt2, 70)
insertBstNode(bt2, 50)
insertBstNode(bt2, 90)
insertBstNode(bt2, 30)
insertBstNode(bt2, 60)
insertBstNode(bt2, 80)
insertBstNode(bt2, 100)
insertBstNode(bt2, 20)
insertBstNode(bt2, 40)
print(bt2)
#Traversal
print('printing preorder->')
preOrderTraversal(bt2)
print()
print('printing inorder->')
inOrderTraversal(bt2)
print()
print('printing postorder->')
postOrderTraversal(bt2)
print()
print('printing levelorder->')
levelOrderTraversal(bt2)
print()