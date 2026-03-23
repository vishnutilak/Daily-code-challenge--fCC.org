def has_no_repeats(s):

    last_char = ""
    for ch in s:
        if ch == last_char:
            return False
        last_char =ch
    return True
