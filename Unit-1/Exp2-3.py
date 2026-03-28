def fact(n):
    if n in [0,1]:
        return 1
    return n * fact(n-1)

def main():
    n = int(input("Enter number to find factorial"))
    x = fact(n)
    print(x)

main()

'''
Space complexity is O(n) as each recursive call adds 1 stack frame. There are n recursive stack calls.
Time complexity is O(n) as total n recursive stack calls are evaluated. There is extra const. time for base case or multiplications which can be ignored.
'''