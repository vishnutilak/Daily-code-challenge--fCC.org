def sum_letters(s):
    total =0
    for ch in s:
        if ch.isalpha():
            total += ord(ch.lower())-ord('a') + 1
    
    return total
