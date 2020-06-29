items = [4, 1, 5, 3, 2]

# Time Complexity O(nlogN)
# Space Complexity O(n)
def merge(data):
    result = []
    if len(data) < 2:
        return data
    l_left = len(data) // 2
    l_right = len(data) - l_left
    left = merge(data[:l_left])
    right = merge(data[l_left:])
    i = j = 0
    while i < l_left and j < l_right:
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result

sortItems = merge(items)
print(items)
print(sortItems)
