def difference(arr1, arr2):
    freq = {}

    for item in arr1:
        freq[item] = freq.get(item, 0) + 1

    for item in arr2:
        freq[item] = freq.get(item, 0) + 1

    result = []


    for item in arr1:
        if freq[item] == 1:
            result.append(item)

    for item in arr2:
        if freq[item] == 1:
            result.append(item)

    return result
