class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node
        
    
    def pop(self):
        if self.head is None:
            return None
        output = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return output

    def top(self):
        return self.head.data 

    def empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        self.queue2.push(value)
        while not self.queue1.empty():
            self.queue2.push(self.queue1.pop())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.pop()

    def top(self):
        return self.queue1.top()

    def empty(self):
        return self.queue1.empty()
