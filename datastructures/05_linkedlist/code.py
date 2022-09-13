class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data


# push(data)-> add a new node on beginning of linkedlist
# insertAt -> insert in given position
# append -> append as new tail
# insertAfter
class LinkedList:

    def __init__(self):
        self.head = None;
        self.size = 0;

    def insert(self, data):
        new = Node(data)
        # Insert data into head
        if self.head is None:
            print('Inserting First Element')
            self.head = new
            self.size += 1
            return
        else:
            print('Inserting New Tail Element')
            current = self.head
            print('Current Initial :', current.data)
            while current.next is not None:
                current = current.next
                print('Current Moved :', current.data)
            current.next = new
            self.size += 1
            return

    def push(self, data):
        new = Node(data)
        # Insert data into head
        new.next = self.head
        self.head = new
        self.size += 1
        return

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.size += 1
            return
        else:
            current = self.head;
            while current.next is not None:
                current = current.next

            current.next = new
            self.size += 1
            return



    def insertAfter(self, new_data, node_data):
        new = Node(new_data)
        if node_data is None:
            print("Error - Give node is Null")
            return
        else:
            #check node is inside Linked list
            current = self.head
            present = True if current.data == node_data else False
            while current.next is not None and present is False:
                current = current.next
                present = True if current.data is node_data else False

            if present is False:
                print("Error - Give node doesnt belong to linked list")
                return
            else :
                #make next of new as next of current node
                new.next = current.next
                #make next of current node as new
                current.next = new
                self.size += 1
                return


    #Position start from 1
    def insertAt(self, data, position):
        new = Node(data)
        if position > self.size or position == 0:
            print("Error - Invalid Position :", position)
            return
        else:
            pointedItem = self.head
            if position == 1:
                self.head= new
                new.next = pointedItem
                self.size += 1
                return
            else:
                for i in range(1, position-1):
                    pointedItem = pointedItem.next

                next = pointedItem.next;
                pointedItem.next = new
                new.next = next
                self.size += 1
                return

    def delete(self, position):
        if self.head is None:
            print("Linked list is empty")
            return
        elif position > self.size or position == 0:
            print("Invalid Position")
            return
        else:
            if position == 1:
                newHead = self.head.next
                removeItem = self.head
                self.head = newHead
                removeItem= None
                self.size -= 1
            else:
                prev = None
                current = self.head
                for i in range(1, position):
                    prev = current;
                    current = current.next

                if current is None:
                    return

                prev.next = current.next
                current=None
                self.size -= 1





    def traverse(self):
        result = ('' if self.head.data is None else str(self.head.data))
        current = self.head
        while current.next is not None:
            result = result + ', '
            current = current.next
            result = result + str(current.data)
        return result




test = LinkedList()
print(test.head)
n1 = 'Sunday'
n2 = 'Monday'
n3 = 'Tuesday'
n4 = 'Wednesday'
n5 = 'Thursday'
n6 = 'Friday'
n7 = 'Saturday'

#test.insert(n4)
#print(test.head)

#test.append(n5)
test.insert(n5)
print(test.head.next)
test.insert(n6)
print(test.head.next.next)
print(test.size)
print('Traversing1 :', test.traverse())
test.push('Monday')
print('Traversing2 :', test.traverse())
test.insertAt('Sunday',0)
print('Traversing3 :', test.traverse())
test.insertAt('Sunday',1)
print('Traversing4 :', test.traverse())
print('Head :', test.head)
test.insertAt('Saturday',6)
print('Traversing5 :', test.traverse())
test.insertAt('Tuesday',3)
print('Traversing6 :', test.traverse())
test.insertAfter('Wednesday', 'Test')
print('Traversing7 :', test.traverse())
test.insertAfter('Wednesday', 'Tuesday')
print('Traversing8 :', test.traverse())
test.append('Saturday')
print('Traversing9 :', test.traverse())
print(test.size)



#Testing Remove
test.delete(0)
print('Traversing10 :', test.traverse())
test.delete(8)
print('Traversing11 :', test.traverse())
test.delete(1)
print('Traversing12 :', test.traverse())
print(test.size)
test.delete(4)
print('Traversing13 :', test.traverse())
print(test.size)
test.delete(5)
print('Traversing14 :', test.traverse())
print(test.size)