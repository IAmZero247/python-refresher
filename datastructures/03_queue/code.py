

#FIFO
class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item);

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            self.queue.pop(0)

    def  peek(self):
        if len(self.queue) == 0:
            return None;
        else:
            return self.queue[0]

    def __str__(self):
        return self.queue[::].__str__();


test =  Queue();
test.enqueue(3)
print('peeking1 :', test.peek()) #3
test.enqueue(2)
print('peeking2 :', test.peek()) #3
test.enqueue(1)
print('peeking3 :', test.peek()) #3
print('printing1 :',test)
test.dequeue()
print('printing2 :' ,test)
print('peeking4 :', test.peek()) #2
test.dequeue()
print('printing3 :' ,test)
print('peeking5 :', test.peek()) #1
test.dequeue()
print('printing4 :' ,test)
print('peeking6 :', test.peek()) #None
test.dequeue()
print('printing5 :' ,test)
print('peeking7 :', test.peek()) #None

