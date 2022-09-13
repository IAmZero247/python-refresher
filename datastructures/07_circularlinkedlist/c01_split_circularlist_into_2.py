import  math

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

    @property
    def split(self):

        if self.size == 0:
            return None
        if self.size == 1:
            return [self, None]

        mid = math.ceil(self.size/2)
        result = []
        count =0;
        curr = self.head
        prev = None
        while curr and count < mid:
            prev = curr
            curr = curr.next
            count = count+1

        tail = prev
        tail.next = self.head
        #current (now) is pointing to head of second linked list
        result.append(self)
        cl2 = CLinkedList()
        count = mid
        while curr and count < self.size:
            cl2.push(curr.data)
            curr = curr.next
            count = count+1
        result.append(cl2)
        return result;




test = CLinkedList()
print('Initial Size',test.size)
print('Traversing0 :', test.traverse())
print(test.head)
test.push('c')
test.push('b')
test.push('a')
print('Traversing1 :', test.traverse())
print('Size1:', test.size)
test.append('Y')
test.append('Z')
print('Size2:', test.size)
print('Traversing2 :', test.traverse())

splitResultList= test.split
if splitResultList is None:
    print(splitResultList)
else:
    for i in splitResultList:
        printVal = i.traverse() if i is not None else None
        print('Traversing Items :',printVal)
