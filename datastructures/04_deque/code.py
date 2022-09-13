

#Doubly Ended Queue
#  1. Input Restricted Dequeue
#  2. Output Restricted Dequeue
class Deque:

    def __init__(self):
        self.queue = []


    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


    def addFirst(self, item):
        self.queue.insert(0, item)

    def addLast(self, item):
        self.queue.append(item)

    def removeFirst(self):
        if(self.size()>0):
            self.queue.pop(0)


    def removeLast(self):
        if (self.size() > 0):
            self.queue.pop()

    def peekFirst(self):
        if(self.size()>0):
           return  self.queue[0]
        else:
            return None

    def peekLast(self):
        if (self.size() > 0):
            return self.queue[-1]
        else:
            return None

    def __str__(self):
        return self.queue[::].__str__();




test = Deque()
print('size :' , test.size())
print('isEmpty :' , test.isEmpty())

test.addFirst(10)
test.addFirst(20)
test.addLast(30)
test.addLast(40)
print('printing1 :',test) #20 10 30 40
print('peeking1 :', test.peekFirst()) #20
print('peeking2 :', test.peekLast()) #40
test.removeFirst()
test.removeLast()
print('printing2 :',test) #10 30
print('peeking3 :', test.peekFirst()) #10
print('peeking4 :', test.peekLast()) #30
print('size :' , test.size())
print('isEmpty :' , test.isEmpty())

test.addFirst(50)
print('printing3 :',test) #50 10 30
test.removeLast()
test.removeFirst()
print('printing4 :',test) #10
print('peeking5 :', test.peekFirst()) #10
print('peeking6 :', test.peekLast()) #10
test.removeFirst()
test.removeFirst()
test.removeFirst()
test.removeLast()
test.removeLast()
test.removeLast()
print('printing5 :',test) #[]
print('peeking7 :', test.peekFirst()) #None
print('peeking8 :', test.peekLast()) #None
print('size :' , test.size())
print('isEmpty :' , test.isEmpty())


