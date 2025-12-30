def string_sum(s):
    total =0
    current =0
    for ch in s:
        if ch.isdigit():
            current = current*10 + int(ch)
        else:
            total+= current
            current =0
    total+= current ##fence post logic?
    return total
