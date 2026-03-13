def smallest_gap(s):
    storage ={}
    min_length = float('inf')
    
    for j,letter in enumerate(s):

        if letter in storage:
            i= storage[letter]
            gap = j-i-1
            if gap<min_length:
                min_length = gap
                result = s[i+1:j]
        storage[letter] = j
    return result
