class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1
        print(f"Appended {value} -> size: {self.size}, capacity: {self.capacity}")

    def resize(self):
        old_capacity = self.capacity
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        print(f"Resized from {old_capacity} to {self.capacity}")

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return

        val = self.arr[self.size - 1]
        self.size -= 1
        print(f"Popped {val} -> size: {self.size}, capacity: {self.capacity}")

da = DynamicArray()

da.append(10)
da.append(20)
da.append(30)
da.append(40)

da.pop()
da.pop()

da.append(50)
da.append(60)