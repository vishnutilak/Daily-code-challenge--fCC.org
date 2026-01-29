def flatten(arr):
    res = []

    for item in arr:
        if isinstance(item, list):
            res.extend(flatten(item))
        else:
            res.append(item)

    return res
