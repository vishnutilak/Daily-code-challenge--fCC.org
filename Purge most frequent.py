def purge_most_frequent(arr):
    freq={}
    ##key value pairs like seen[] list
    
    for element in arr:
        if element in freq:
            freq[element]+=1
        else:
            freq[element]=1
    
    max_freq=0
    for count in freq.values():
        if count> max_freq:
            max_freq= count
    
    result =[]
    for element in arr:
        if freq[element] != max_freq:
            result.append(element)
     
    return result


"""Purge Most Frequent

Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

    If multiple values are tied for most frequent, remove all of them.
    Do not change any of the other elements or their order.

"""
