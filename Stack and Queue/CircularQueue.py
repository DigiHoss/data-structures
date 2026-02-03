class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if (self.rear + 1) % self.size  == self.front:
            print("Queue is full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else :
            self.front = (self.front + 1) % self.size
            return item
        
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        
        i = self.front
        print("Queue : ", end="")
        while True:
            print(self.queue[i], end="")

            if i == self.rear:
                break
            i = (i+1) % self.size
        print()


def test():
    cq = CircularQueue(4)
    cq.enqueue('A')
    cq.enqueue('B')
    cq.enqueue('C')
    cq.enqueue('D')
    cq.display()
    cq.enqueue('E')
    cq.display()


if __name__ == '__main__':
    test()