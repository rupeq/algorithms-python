items = [2, 3, 5, 6, 11, 13, 16]

def interp_search(lst, x):
    low = 0
    high = len(lst) - 1
    lower = lst[low]
    higher = lst[high]
    while lower < x < higher:
        mid = low + ((x - lower) * (high - low)) // (higher - lower)
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return f'Found it! Place - {mid}'
    if lower == x:
        return f'Found it! Place - {low}'
    if higher == x:
        return f'Found it! Place - {high}'
    return None

print(interp_search(items, 5))
