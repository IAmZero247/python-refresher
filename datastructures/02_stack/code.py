

#LIFO
class Stack:

    def __init__(self):
        self.stack = [];

    # add an element
    def push(self, value):
        self.stack.append(value)
        print(value , " added to 02_stack")

    # remove top most element
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop();
        #   del(self.stack[-1])


    # read top most element
    def peek(self):
        if len(self.stack) == 0:
            return None;
        else:
            return self.stack[-1]

    def __str__(self):
        return self.stack[::].__str__()




test =  Stack();
test.push(3)
print('peeking :', test.peek())
test.push(2)
print('peeking :', test.peek())
test.push(1)
print('peeking :', test.peek())
test.pop()
print('peeking :', test.peek())
test.pop()
test.pop()
print('peeking :', test.peek())
test.pop()
print('peeking :', test.peek())

