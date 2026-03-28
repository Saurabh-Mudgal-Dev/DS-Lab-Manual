class nodeSLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_at_end(self, data):
        new_node = nodeSLL(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def insert_at_start(self, data):
        new_node = nodeSLL(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def delete_by_index(self, ind):
        curr = self.head
        if curr and ind == 0:
            self.head = curr.next
            return
        curr = self.head.next
        i = 1
        while i < ind-1:
            curr = curr.next
            i += 1
            curr.next = curr.next.next
    
    def delete_by_val(self, data):
        curr = self.head
        if curr and curr.data == data:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

L= [1,2,3,4,5]
My_List= SLL()
for i in L:
    My_List.insert_at_end(i)
My_List.delete_by_val(2)
My_List.delete_by_index(3)
print(My_List)
print(My_List.traverse())