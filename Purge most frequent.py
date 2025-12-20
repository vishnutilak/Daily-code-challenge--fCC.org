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
