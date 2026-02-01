class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end="<->")
            current = current.next
        print("None")


def test ():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.display()

if __name__ == '__main__':
    test()


