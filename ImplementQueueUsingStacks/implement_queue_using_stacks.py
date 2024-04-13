class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        elif not self.tail:
            self.tail = self.head
            self.head = new_node
            self.head.next = self.tail
        else:
            next = self.head
            self.head = new_node
            self.head.next = next

    
    def pop(self):
        if not self.head:
            return None
        if not self.tail:
            output = self.head.data
            self.head = None
            return output
        if self.head == self.tail:
            output = self.tail.data
            self.head = None
            self.tail = None
            return output
        current = self.head
        while current and current.next != self.tail:
            current = current.next
        if current:
            output = self.tail.data
            current.next = None
            self.tail = current
            return output
        else:
            return None

    def top(self):
        if self.tail:
            return self.tail.data
        return self.head.data

    def empty(self):
        return self.head is None

class MyQueue:

    def __init__(self):
        self.queue1 = Stack()
        self.queue2 = Stack()

    def push(self, x: int) -> None:
        self.queue2.push(x)
        while not self.queue2.empty():
            self.queue1.push(self.queue2.pop())

    def pop(self):
        return self.queue1.pop()
    
    def peek(self):
        return self.queue1.top()

    def empty(self):
        return self.queue1.empty()
