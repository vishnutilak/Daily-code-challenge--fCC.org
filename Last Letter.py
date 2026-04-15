def get_last_letter(s):
    
    max_char = ''

    for ch in s:
        if ch.isalpha():
            if max_char =='' or ch.lower()>max_char.lower():
                    max_char = ch
    return max_char
