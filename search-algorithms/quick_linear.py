items = [2, 3, 5, 6, 11, 13, 16]

def linear_search(lst, x):
    i = 0
    count = len(lst)
    lst.append(x)
    while True:
        if lst[i] == x:
            del lst[count]
            return f'Found it! Place - {i}' if i < count else None
        i += 1

print(linear_search(items, 5))
