def most_frequent(arr):
    freq ={}
    max_count =0
    result = None

    for item in arr:
        if item in freq:
            freq[item] +=1
        else:
            freq[item] =1
        if freq[item] >max_count:
            max_count = freq[item]
            result = item
    return result
