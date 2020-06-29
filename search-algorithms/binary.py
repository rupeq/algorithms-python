items = [2, 3, 5, 6, 11, 13, 16]

# only for sorted
def bin_search(lst, x):
    i = 0
    j = len(lst)
    while i!= j:
        m = (i + j) // 2
        if x == lst[m]:
            return f"Found it! Place - {m}"
        if x < lst[m]:
            j = m
        else:
            i = m + 1
    return 'Not in the list'

print(bin_search(items, 16))
