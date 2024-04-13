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
        next = self.head
        self.head = new_node
        self.tail = next
    
    def pop(self):
        if self.head is None:
            return None
        output = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return output

    def top(self):
        return self.head.data if self.head else None

    def empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.stack = Queue()

    def push(self, value):
        self.stack.push(value)
        if self.stack.tail and self.stack.head:
            current = self.stack.head
            while current.next:
                current = current.next
            self.stack.head.next = self.stack.tail
    
    def pop(self):
        if self.empty():
            return None
        if self.stack.head:
            output = self.stack.head.data
            if self.stack.tail:
                self.stack.tail = self.stack.tail.next
            self.stack.head = self.stack.head.next
        elif self.stack.tail:
            output = self.stack.tail.data
            self.stack.head = None
        return output
    
    def top(self):
        return self.stack.head.data if self.stack.head else self.stack.tail.data
    
    def empty(self):
        return self.stack.empty()
  
