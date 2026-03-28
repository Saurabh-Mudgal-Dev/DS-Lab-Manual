def loops(n):

    # single loop
    print("Estimated count:", n)
    for i in range(n):
        print("*", end = " ")
    print()
    print("Time complexity: O(n) as loops runs 0 to n-1, that is n times")
    print()
    
    # nested loop
    print("Estimated count:", n**2)
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
    print()
    print("Time complexity: O(n^2) as at each iteration of i, j runs n times and i also runs n times so they get multiplied")
    print()
    
    # triangular loop
    print("Estimated count:", n*(n-1)/2)
    for i in range(n):
        for j in range(i):
            print("*", end = " ")
    print()
    print("Time complexity: O(n^2) as i runs n times and j runs i times at each iteration, \n Number of iterations becomes 1+2+3+...+n-1 which is n(n-1)/2 \n this is a quadratic with highest power 2, thus the complexity")
    print()
    
    # halving loop
    print(f"Estimated count: log2({n}) + 1") # loop runs once before halving starts so 1 is added to expected iterations
    while n > 0:
        print("*", end = " ")
        n = n // 2
    print()
    print("Time complexity: O(log2(n)) as at each step, we half n until it becomes 0, thus decreasing n multiplicatively")

loops(10)

'''
for linear search:
    best case is Ω(1) if first element matches target
    worst case is O(n) if last element matches target
    average case is Θ(n/2) or Θ(n) if element found in middle, 1/2 is const. so ignored

for binary search:
    best case is Ω(1) if middle element is target
    worst case is O(logn) if target is not present or is at deepest level of search tree
    average acse is Θ(logn) as the lowest level of binary tree contains the most elements so on avg., target should be at bottom-most level
'''