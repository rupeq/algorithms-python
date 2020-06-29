import math

items = [2, 3, 5, 6, 11, 13, 16]

def jump_search(arr, x):
    length = len(arr)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and arr[left] <= x:
        right = min(length - 1, left + jump)
        if arr[left] <= x and arr[right] >= x:
            break
        left += jump
    if left >= length or arr[left] > x:
        return print(f'{x} is not in array')
    right = min(length - 1, right)
    count = left
    while count <= right and arr[count] <= x:
        if arr[count] == x:
            return print(f'{x} has found')
        count += 1
    return print(f'{x} is not in array')

jump_search(items, 6)
