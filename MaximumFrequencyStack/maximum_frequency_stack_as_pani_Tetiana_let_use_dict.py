from collections import deque

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.frequency = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.frequency[val] = self.frequency.get(val, 0) + 1
    
    def pop(self) -> int:
        max_freq = max(self.frequency.values())
        max_freq_elements = [element for element, freq in self.frequency.items() if freq == max_freq]
        self.stack.reverse()
        for element in self.stack:
            if element in max_freq_elements:
                self.stack.remove(element)
                self.frequency[element] -= 1
                if self.frequency[element] == 0:
                    del self.frequency[element]
                self.stack.reverse()
                return element
