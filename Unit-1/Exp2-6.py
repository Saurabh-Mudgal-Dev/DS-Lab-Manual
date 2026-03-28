def binsearch_rec(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    # if target larger than mid, go check the right
    elif arr[mid] < target:
        return binsearch_rec(arr, target, mid+1, high)
    # if target smaller, then go check the left
    return binsearch_rec(arr, target, low, mid-1)
# Time complexity is O(logn) as array is halved at every single step
# Space complexity is O(logn) because of recursive call stack depth

arr = sorted(eval(input("Enter array of elements")))
target = int(input("Enter the target to be found"))
x = binsearch_rec(arr, target, 0, len(arr)-1)
print(f"Index of {target} is {x}")