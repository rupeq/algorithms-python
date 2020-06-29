items = [4, 1, 5, 3, 2]

# Time Complexity (sqr(O))
# Space Complexity O(1)
def bubble_sort(data):
    lst = list(data)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

sortItems = bubble_sort(items)
print(items)
print(sortItems)
