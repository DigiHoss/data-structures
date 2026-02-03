class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items

def test():
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.dequeue()

    print("Front item : ", q.peek())
    print("Size of queue : ", q.size())
    print(q.display())


    
# to use built in queue data structures
from collections import deque

def discover():
    new_q = deque()
    new_q.append('A')
    new_q.append('B')
    new_q.append('C')
    new_q.popleft()
    print(new_q)

if __name__ == '__main__':
    test()
    discover()