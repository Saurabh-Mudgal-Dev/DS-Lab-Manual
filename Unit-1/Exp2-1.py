class StackADT():
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data) == 0
    def push(self, ele):
        self.data.append(ele)
    def pop(self):
        if self.data == []:
            return "Empty"
        return self.data.pop()
    def peek(self):
        if self.data == []:
            return "Empty"
        return self.data[-1]
    def size(self):
        return len(self.data)

def main(commands : list[str]):
    st = StackADT()
    outputs = []

    for cmd in commands:
        parts = cmd.strip().split()
        match parts[0]:
            case "PUSH":
                st.push(int(parts[1]))
            case "POP":
                outputs.append(str(st.pop()))
            case "PEEK":
                outputs.append(str(st.peek()))
            case "ISEMPTY":
                outputs.append(str(st.isEmpty()))
            case "SIZE":
                outputs.append(str(st.size()))
    return "\n".join(outputs)

x = main(["PUSH 5", "PUSH 10", "PEEK", "PUSH 4", "SIZE", "POP", "POP", "PEEK", "ISEMPTY"])
print(x)

# small use case: check if brackets are placed correctly or not
def bracket_balanced(expr : str):
    st = StackADT()
    for i in expr:
        if i == "(":
            st.push(i)
        elif i == ")":
            if st.isEmpty():
                return False
            st.pop()
    return st.size() == 0

print(bracket_balanced("(1+2)-(9*4)"))