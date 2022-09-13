class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return '' if self.data is None else str(self.data)

    def __eq__(self, other):
        return str(self.data) == str(other.data)

class DLinkedList():

    def __init__(self):
        self.head = None
        self.size = 0

    def __sizeof__(self):
        return self.size

    def traverse(self):
        current = self.head
        result = ''
        while current :
            result = result if current is self.head else result+','
            result = result+'' if current.data is None else result+str(current.data)
            current = current.next
        return result

    def traverseBack(self):
        current = self.head

        tail = None
        while current:
            tail=current;
            current = current.next
        prev = tail
        result = ''
        while prev:
            result = result if prev is tail else result + ','
            result = result + '' if prev.data is None else result + str(prev.data)
            prev = prev.prev
        return result

    def push(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.size =self.size+1
            return
        else :
            nextNode = self.head
            new.next =nextNode
            nextNode.prev = new
            self.head = new
            self.size = self.size+1
            return


    def insertAfter(self, newData, nodeData):
        new = Node(newData)
        current = self.head
        datamatch = False
        previous = None
        while current:
            previous = current
            if current.data is nodeData:
                print(current.data)
                datamatch = True
                break
            current = current.next

        if datamatch is False:
            print('No Match')
            return
        else:
            nextNode = current.next
            isNextNodeIsNone= True if nextNode is None else False
            #if true , new element becomes tail of DlinkedList
            if isNextNodeIsNone:
                new.prev = current
                current.next = new
                self.size = self.size + 1
                return
            else:
                nextNode.prev = new
                new.next = nextNode
                new.prev=current
                current.next = new
                self.size = self.size+ 1
                return



    def insertAt(self, newData, position):
        new = Node(newData)
        if position > self.__sizeof__() or position == 0:
            print('Invalid Position')
        else:
            current = self.head
            iteration = 1
            while current and iteration != position:
                current = current.next
                iteration = iteration + 1;

            print('current:', current.data)
            if position == 1 :
                current.prev = new
                new.next = current
                self.head = new
                self.size = self.size + 1
                return
            else:
                previous  = current.prev
                print('previous :', previous)
                new.prev = previous
                new.next = current
                current.prev=new
                previous.next=new
                self.size = self.size + 1
                return

    def append(self ,data):
        new = Node(data)
        if self.head is None:
            self.head=new
            self.size = self.size + 1
            return
        else:
            current = self.head
            last = None
            while current:
                last = current
                current = current.next
            last.next=new
            new.prev=last
            self.size = self.size + 1
            return


    def deleteAt(self, position):
        if position > self.size:
            print("Invalid Position")
        else:
            current = self.head
            counter =1
            prev = None
            while current and counter is not position:
                prev =current
                current = current.next if current is not None else None
                counter = counter+1
            if prev is None:
                nextNode = current.next if current is not None else None
                self.head = nextNode
                self.head.prev=None
                current=None
                self.size = self.size-1
                return
            else:
                nextNode = current.next if current is not None else None
                prev.next = nextNode
                if nextNode is not None:
                    nextNode.prev = prev
                current = None
                self.size = self.size - 1
                return



    def delete(self, data):
        current = self.head
        #check head is matching
        if current.data is data:
            nextNode = current.next if current.next is not None else None
            if nextNode is not None:
                nextNode.prev=None
            self.head=nextNode
            current =None
            self.size = self.size - 1
        #iterate for matching
        else:
            prev = None
            isMatch = False
            while current:
                prev = current
                current = current.next if current is not None else None
                if current is not None and current.data is data:
                    isMatch =True
                    break
            if isMatch is False:
                print('No Match')
                return
            nextNode= current.next if current is not None else None
            prev.next = nextNode
            if nextNode is not None:
                nextNode.prev = prev
            current = None
            self.size = self.size-1
            return















test = DLinkedList()
print('Initial Head :', test.head)
n1 = 'Sunday'
n2 = 'Monday'
n3 = 'Tuesday'
n4 = 'Wednesday'
n5 = 'Thursday'
n6 = 'Friday'
n7 = 'Saturday'
test.append("One" )
print('Traversing Forward 1 :', test.traverse())
print('Traversing Back 1 :', test.traverseBack())
print('Size1 :' , test.__sizeof__())
test.push('Wednesday')
print('Traversing Forward 2 :', test.traverse())
print('Traversing Back 2 :', test.traverseBack())
print('Size2 :' , test.__sizeof__())
test.push('Sunday')
print('Traversing Forward 3 :', test.traverse())
print('Traversing Back 3 :', test.traverseBack())
print('Size3 :' , test.__sizeof__())
test.insertAfter( 'Monday' , 'Sunday')
test.insertAfter( 'Thursday' , 'Wednesday')
print('Traversing Forward 4 :', test.traverse())
print('Traversing Back 4 :', test.traverseBack())
print('Size4 :' , test.__sizeof__())
test.insertAt("Sample" ,0)
test.insertAt("Tuesday", 4)
print('Traversing Forward 5 :', test.traverse())
print('Traversing Back 5 :', test.traverseBack())
print('Size5 :' , test.__sizeof__())
test.append("Friday" )
print('Traversing Forward 6 :', test.traverse())
print('Traversing Back 6 :', test.traverseBack())
print('Size6 :' , test.__sizeof__())
test.deleteAt(1)
print('Traversing Forward 7 :', test.traverse())
print('Traversing Back 7 :', test.traverseBack())
print('Size7 :' , test.__sizeof__())
test.deleteAt(2)
print('Traversing Forward 8 :', test.traverse())
print('Traversing Back 8 :', test.traverseBack())
print('Size8 :' , test.__sizeof__())
test.deleteAt(4)
print('Traversing Forward 9 :', test.traverse())
print('Traversing Back 9 :', test.traverseBack())
print('Size9 :' , test.__sizeof__())
test.delete('Something')
test.delete('Friday')
print('Traversing Forward 10 :', test.traverse())
print('Traversing Back 10 :', test.traverseBack())
print('Size10 :' , test.__sizeof__())
test.delete('Tuesday')
print('Traversing Forward 11 :', test.traverse())
print('Traversing Back 11 :', test.traverseBack())
print('Size11 :' , test.__sizeof__())
test.delete('Thursday')
print('Traversing Forward 12 :', test.traverse())
print('Traversing Back 12 :', test.traverseBack())
print('Size12 :' , test.__sizeof__())
test.delete('Monday')
print('Traversing Forward 13 :', test.traverse())
print('Traversing Back 13 :', test.traverseBack())
print('Size13 :' , test.__sizeof__())