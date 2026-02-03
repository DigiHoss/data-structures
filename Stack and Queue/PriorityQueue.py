class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item, priority):
        self.queue.append((priority,item))

    def dequeue(self):
        if self.is_empty():
            return None
        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i

        return self.queue.pop(min_index)
    
    def peek(self):
        if self.is_empty():
            return None
        return min(self.queue, key=lambda x:x[0])
    

def test():
    pq = PriorityQueue()
    pq.enqueue("Task A", 3)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 4)
    pq.enqueue("Task D", 2)
    print("Next task : ", pq.peek())
    print("Dequeued : ", pq.dequeue())
    print("Next tast : ", pq.peek())


if __name__ == '__main__':
    test()