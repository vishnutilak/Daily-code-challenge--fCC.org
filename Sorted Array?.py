def is_sorted(arr):
    n= len(arr)-1

    descending = True
    ascending = True

    for i in range(n):
        if arr[i]<arr[i+1]:
            descending = False
        if arr[i]>arr[i+1]:
            ascending = False


    if ascending  and not descending:
        return "Ascending"
    if descending  and not ascending:
        return "Descending"
    return "Not sorted"
