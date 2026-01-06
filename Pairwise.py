def pairwise(arr, target):
    used = set()
    index_map = {}
    total = 0

    for i in range(len(arr)):
        if i in used:
            continue

        complement = target - arr[i]

        if complement in index_map and index_map[complement] not in used:
            j = index_map[complement]

            total += i + j
            used.add(i)
            used.add(j)

            # remove to prevent further reuse
            del index_map[complement]
        else:
            index_map[arr[i]] = i

    return total
