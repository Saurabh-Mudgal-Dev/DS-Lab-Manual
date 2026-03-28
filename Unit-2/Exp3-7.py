class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.front())

print("Dequeued:", q.dequeue())
print("Front:", q.front())

q.enqueue(40)
q.enqueue(50)

print("Dequeued:", q.dequeue())

print("Final Queue:")
q.display()