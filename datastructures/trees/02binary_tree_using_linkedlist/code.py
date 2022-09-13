import queue
class BTNode:

    def __init__(self, data, left: 'BTNode' = None, right: 'BTNode' = None):
        self.data = data
        self.left = left
        self.right = right

    def addLeft(self, node: 'BTNode'):
        self.left = node

    def addRight(self, node: 'BTNode'):
        self.right = node

    def __str__(self, level=0):
        startwith = " " if level == 0 else "--"
        ret = (startwith * level) + '> ' + str(self.data) + "\n"
        if(self.left is not None):
            ret += self.left.__str__(level+1)
        if (self.right is not None):
            ret += self.right.__str__(level+1)
        return ret

#Helpers For BTree
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data , '> ', end='')
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)
    return None

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data, '> ', end='')
    inOrderTraversal(rootNode.right)
    return None

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data, '> ', end='')
    return None

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    qu = queue.Queue()
    qu.enqueue(rootNode)
    while(not qu.isEmpty()):
        element = qu.dequeue()
        print(element.value.data, '> ', end='')
        if(element.value.left is not None):
            qu.enqueue(element.value.left)
        if (element.value.right is not None):
            qu.enqueue(element.value.right)
    return None

def search(rootNode, value):
    if not rootNode:
        return 'BTree doesnt exists'
    qu = queue.Queue()
    qu.enqueue(rootNode)
    while(not qu.isEmpty()):
        element = qu.dequeue()
        if element.value.data is value:
            return 'Success'
        if element.value.left is not None:
            qu.enqueue(element.value.left)
        if element.value.right is not None:
            qu.enqueue(element.value.right)
    return 'Failure'


def insertBtNode(rootNode, node):
    if not rootNode:
        rootNode = node
        return rootNode
    qu = queue.Queue()
    qu.enqueue(rootNode)
    while (not qu.isEmpty()) :
        element = qu.dequeue()
        if(element.value.left is None):
            element.value.left = node
            return element.value.left
        else:
            qu.enqueue(element.value.left)
        if (element.value.right is None):
            element.value.right = node
            return element.value.right
        else:
            qu.enqueue(element.value.right)
    return None

#DeleteNode
##Helper1 -> getDeepestNode
def getDeepestNode(rootNode):
    if not rootNode:
        return None
    qu = queue.Queue()
    qu.enqueue(rootNode)
    while (not qu.isEmpty()):
        element = qu.dequeue()
        if element.value.left is not None:
            qu.enqueue(element.value.left)
        if element.value.right is not None:
            qu.enqueue(element.value.right)
    return element.value
##Helper2 -> deleteDeepestNode
def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return None
    if not deepestNode:
        return None
    qu = queue.Queue()
    qu.enqueue(rootNode)
    while (not qu.isEmpty()):
        element = qu.dequeue()
        if element is deepestNode:
            element.value = None
        if element.value.left is not None:
            if element.value.left is deepestNode:
                element.value.left =None
            else:
                qu.enqueue(element.value.left)
        if element.value.right is not None:
            if element.value.right is deepestNode:
                element.value.right = None
            else:
                qu.enqueue(element.value.right)
    return None
#deleteNodeBT

def deleteBTNode(rootNode, btNodeData):
    if not rootNode:
        return 'Binary Tree Doesnt Exist'
    if not btNodeData:
        return 'Given BtNodeData is None'
    qu = queue.Queue()
    qu.enqueue(rootNode)
    deepestNode= getDeepestNode(rootNode)
    while (not qu.isEmpty()):
        element = qu.dequeue()
        if element.value.data is btNodeData:
            element.value.data = deepestNode.data
            deleteDeepestNode(rootNode,deepestNode)
            return 'The Node Has Been Successfully Deleted'
        if element.value.left is not None:
            qu.enqueue(element.value.left)
        if element.value.right is not None:
            qu.enqueue(element.value.right)
    return 'Failed to delete node'

#deleteBT
def deleteBT(rootNode):
    if rootNode is None:
        return 'Binary Tree Doesnt Exist'
    else:
        rootNode.data = None
        rootNode.left= None
        rootNode.right = None
        return 'Succesfully Deleted BTree'

#Binary Tree
rootNode = BTNode('N1')
lN1 = BTNode('N2')
rN1 = BTNode('N3')
rootNode.addLeft(lN1)
rootNode.addRight(rN1)
lN2 = BTNode('N4')
rN2 = BTNode('N5')
lN1.addLeft(lN2)
lN1.addRight(rN2)
lN5 = BTNode('N8')
rN5 = BTNode('N9')
lN2.addLeft(lN5)
lN2.addRight(rN5)
lN3 = BTNode('N6')
rN3 = BTNode('N7')
rN1.addLeft(lN3)
rN1.addRight(rN3)
print(rootNode)
#Traversal
print('printing preorder->')
preOrderTraversal(rootNode)
print()
print('printing inorder->')
inOrderTraversal(rootNode)
print()
print('printing postorder->')
postOrderTraversal(rootNode)
print()
print('printing levelorder->')
levelOrderTraversal(rootNode)
print()
#Searching
print('Searching N5 :' , search(rootNode ,'N5'))
print('Searching N12 :' , search(rootNode ,'N12'))
#Insertion
insertBtNode(rootNode, BTNode('N10'))
insertBtNode(rootNode, BTNode('N11'))
levelOrderTraversal(rootNode)
print()
#Deletion
#helper1 is getDeepestNode
#helper2 is deleteDeepestNode
#deleteNode uses above two helpers
deepestNode = getDeepestNode(rootNode)
print('deepest Node :', str(deepestNode.data))
deleteDeepestNode(rootNode, getDeepestNode(rootNode))
levelOrderTraversal(rootNode)
print()
deleteDeepestNode(rootNode, getDeepestNode(rootNode))
levelOrderTraversal(rootNode)
print()
deleteBTNode(rootNode, 'N6')
levelOrderTraversal(rootNode)
print()
deleteBT(rootNode)
levelOrderTraversal(rootNode)
print()
levelOrderTraversal(lN2)