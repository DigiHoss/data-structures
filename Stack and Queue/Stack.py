class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print("Stack from bottom to top")
        for item in self.items:
            print(item)


def test():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Popped :", s.pop())
    s.display()
    print("Top item :", s.peek())
    s.pop()
    s.pop()
    print("Popped again : ", s.pop())

test()