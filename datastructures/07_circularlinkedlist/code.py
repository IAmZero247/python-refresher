
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return '' if self.data is None else str(self.data)

    def __eq__(self, other):
        return str(self.data) == str(other.data)

class CLinkedList():

    def __init__(self):
        self.head = None
        self.size = 0

    def traverse(self):
        current = self.head
        result = ''
        while current:
            result = result + ',' if current is not self.head else result
            result = result + current.data if current is not None else result
            current = current.next
            if current is self.head :
                break
        return result

    def push(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.head.next = self.head
            self.size = self.size+1
            return
        else:
            itrNode = self.head
            while itrNode.next != self.head:
                itrNode = itrNode.next
            itrNode.next = new
            new.next = self.head
            self.head = new
            self.size = self.size + 1
            return

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.head.next = self.head
            self.size = self.size + 1
            return
        else:
            itrNode = self.head
            while itrNode.next != self.head:
                itrNode = itrNode.next
            itrNode.next = new
            new.next = self.head
            self.size = self.size + 1
            return


    def deleteFirst(self):
        if self.head is None:
            return None
        if self.head is self.head.next:
            self.head = None
            self.size = self.size -1
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next=self.head.next
        self.head=curr.next
        self.size = self.size-1
        return


    def deleteLast(self):
        if self.head is None:
            return None
        if self.head is self.head.next:
            self.head = None
            self.size = self.size -1
            return
        curr = self.head
        prev = None
        while curr.next != self.head:
            prev = curr
            curr = curr.next
        curr = None
        prev.next=self.head
        self.size = self.size-1
        return








test = CLinkedList()
print('Initial Size',test.size)
print('Traversing0 :', test.traverse())
print(test.head)
n1 = 'Sunday'
n2 = 'Monday'
n3 = 'Tuesday'
n4 = 'Wednesday'
n5 = 'Thursday'
n6 = 'Friday'
n7 = 'Saturday'
test.push(n1)
print('Head1 :', test.head)
test.push(n2)
print('Head2 :', test.head)

print('Traversing1 :', test.traverse())
print('Size1:', test.size)
test.append(n3)
test.append(n4)
print('Head3 :', test.head)
print('Traversing2 :', test.traverse())
print('Size3:', test.size)
test.deleteFirst()
print('Head4 :', test.head)
print('Traversing4 :', test.traverse())
test.deleteFirst()
print('Head5 :', test.head)
print('Traversing5 :', test.traverse())
test.push(n2)
test.push(n1)
print('Traversing6 :', test.traverse())
print('Size4:', test.size)
test.deleteLast()
print('Traversing7 :', test.traverse())
print('Size5:', test.size)
test.deleteLast()
print('Traversing8 :', test.traverse())
print('Size6:', test.size)