class MyClass:
    """A very simple class :)"""

    def greet(self, name):
        return "Hello, " + name

# c = MyClass()
# print c.greet("Ash :)")

class Queue:

    def __init__(self):
        self.queue = []
    def isempty(self):
        return not bool(self.queue)
        # if self.queue == [] :
        #     return True
        # else:
        #     return False
    def push(self,item):
        self.queue.append(item)

    def pop(self):
        if not self.isempty():
            x= self.queue[0]
            self.queue = self.queue[1:]
            return x

    def toString(self):
        print self.queue


# q = Queue()
# print q.isempty()
# q.push("sup")
# q.push("boi")
# print q.isempty()
# print q.pop()
# q.toString()
# print q.pop()
# q.toString()
# print q.isempty()
class Stack:
    def __init__(self):
        self.stack =[]
    def isempty(self):
        return not bool(self.stack)

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.isempty():
            x= self.stack[-1]
            self.stack = self.stack[:-1]
            return x
    def toString(self):
        print self.stack

s = Stack()
print s.isempty()
s.push("sup")
s.push("boi")
s.push("yo")
print s.isempty()
print s.pop()
s.toString()
print s.pop()
s.toString()
print s.isempty()
print s.pop()
s.toString()
print s.isempty()
