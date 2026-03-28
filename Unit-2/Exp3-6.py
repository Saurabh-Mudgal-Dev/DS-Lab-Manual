class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


def is_valid(s):
    st = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.is_empty() or st.pop() != pairs[ch]:
                return False

    return st.is_empty()

tests = ["()", "([])", "([)]", "{[()]}", "((("]

for t in tests:
    print(t, "->", is_valid(t))