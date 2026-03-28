def hanoi(n, start, spare, end):
    if n == 1:
        print(f"disk 1 moves from {start} to {end}")
        return 1
    x = hanoi(n-1, start, end, spare) # move n-1 disks from start to spare first using end as mediary
    print(f"disk {n} moves from {start} to {end}")
    y = hanoi(n-1, spare, start, end) # then move n-1 disks from spare to end using start as mediary
    return x+1+y # add 1 for remaining one disk
# Time complexity is O(2^n) as number of moves are (2^n)-1 and we can ignore 1 as const.
# Space complexity is O(n ) as max. recursive depth of call stack is no. of disks that is n

n = 3
total_moves = hanoi(n, 'A', 'B', 'C')
print(f"Total moves: {total_moves}")

print(f"The move count for N = 4 is {hanoi(4, 'A', 'B', 'C')}")