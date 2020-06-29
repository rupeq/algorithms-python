items = [4, 1, 5, 3, 2]

# Time complexity from O(nlogN) to (sqr(O))
# Space compexity O(logN)
def quick_sort(data):
    def sort(s_data, fst, lst):
        if fst >= lst:
            return None
        i, j = fst, lst
        x = s_data[(fst + lst) // 2]
        while i <= j:
            while s_data[i] < x:
                i += 1
            while s_data[j] > x:
                j -= 1
            if i <= j:
                s_data[i], s_data[j] = s_data[j], s_data[i]
                i, j = i + 1, j - 1
            sort(s_data, fst, j)
            sort(s_data, i, lst)
        return s_data
    return sort(list(data), 0, len(data) - 1)

sortItems = quick_sort(items)

print(items)
print(sortItems)
