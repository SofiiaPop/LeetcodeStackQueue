from collections import deque

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.freq = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq.append(self.stack.count(val))

    def pop(self) -> int:
        self.freq.reverse()
        index = self.freq.index(max(self.freq))
        self.freq.reverse()
        self.freq.rotate(index)
        self.stack.rotate(index)
        self.freq.pop()
        val = self.stack.pop()
        self.freq.rotate(-index)
        self.stack.rotate(-index)
        return val
