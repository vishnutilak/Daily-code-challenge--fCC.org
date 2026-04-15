def sort_and_swap(arr):
    arr = sorted(arr)

    for i in range(3, len(arr), 3):
        arr[i], arr[i-1] = arr[i-1], arr[i]

    return arr
##############################################
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res


def sort_and_swap(arr):
    arr = merge_sort(arr)
    
    for i in range(3, len(arr), 3):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    
    return arr
