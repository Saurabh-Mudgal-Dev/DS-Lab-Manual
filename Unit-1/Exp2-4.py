ct_naive = 0
def fib_naive(n):
    global ct_naive
    ct_naive += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Time complexity is O(2^n) as for every term, there will be 2 recursive call stacks seperately
# Space complexity is O(n) because of recursive depth of call stack

n = int(input("Enter nth term of fibonacci series to be calculated"))
ct_memo = 0
memo_fib = [-1] * (n+1)
def fib_memo(n):
    global memo_fib
    global ct_memo
    ct_memo += 1
    if memo_fib[n] != -1:
        return memo_fib[n]
    elif n <= 1:
        memo_fib[n] = n
        return n
    memo_fib[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo_fib[n]

# Time complexity is O(n) as each fib. term is calculated only once instead of being calculated for fib_memo(3) and 4 and so on
# Space complexity is O(n) because of recursive depth of call stack

# print(fib_naive(10), ct_naive) : 177 calls
# print(fib_memo(10), ct_memo) : 19 calls

# print(fib_naive(20), ct_naive) : 21891 calls
# print(fib_memo(20), ct_memo) : 39 calls

# print(fib_naive(30), ct_naive) : 2692537 calls
# print(fib_memo(30), ct_memo) : 59 calls