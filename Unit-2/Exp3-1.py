arr = [10, 20, 30, 40, 50]

def get_location(pos, n):
    if pos == 0:
        return "start"
    elif pos >= n:
        return "end"
    else:
        return "middle"

def insert(arr, pos, val):
    shifts = len(arr) - pos
    location = get_location(pos, len(arr))
    arr.insert(pos, val)
    print(f"\nInsert {val} at {location} (index {pos})")
    print(f"Array: {arr}")
    print(f"Shifts: {shifts} → Complexity: {'O(1)' if shifts == 0 else 'O(n)'}")

def delete(arr, pos):
    location = get_location(pos, len(arr))
    shifts = len(arr) - pos - 1
    arr.pop(pos)
    print(f"\nDelete from {location} (index {pos})")
    print(f"Array: {arr}")
    print(f"Shifts: {shifts} → Complexity: {'O(1)' if shifts == 0 else 'O(n)'}")

print("Initial array:", arr)

insert(arr, 0, 99)
insert(arr, len(arr) // 2, 55)
insert(arr, len(arr), 77)

delete(arr, 0)
delete(arr, len(arr) // 2)
delete(arr, len(arr) - 1)