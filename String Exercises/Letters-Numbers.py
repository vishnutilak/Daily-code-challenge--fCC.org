def separate_letters_and_numbers(s):
    if not s:
        return ""

    res =[s[0]]

    for i in range(1,len(s)):
        if s[i-1].isalpha() and s[i].isdigit():
            res.append('-')
            res.append(s[i])
        if s[i-1].isdigit() and s[i].isalpha():
            res.append('-')
            res.append(s[i])
        if (s[i-1].isdigit() and s[i].isdigit()) or (s[i-1].isalpha() and s[i].isalpha()):
            res.append(s[i])
    
    return ''.join(res)

    # for i in range(1, len(s)):
    #     if s[i].isalpha() != s[i - 1].isalpha():
    #         res.append('-')
    #     res.append(s[i])
