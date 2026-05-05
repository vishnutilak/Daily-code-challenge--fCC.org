def is_narcissistic(n):
    str_n = str(n)
    total_sum = 0
    length = len(str_n)
    
    for digit in str_n:
        total_sum += int(digit)**length

    return total_sum== n
