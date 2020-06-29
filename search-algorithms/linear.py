items = [2, 3, 5, 6, 11, 13, 16]

def linear_search(lst, x):
    i = 0
    length = len(lst)
    while i < length:
        if lst[i] == x:
            return f'Found it! Place - {i}'
        i += 1
    return None

print(linear_search(items, 3))
