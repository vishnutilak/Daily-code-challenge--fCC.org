def to_consonant_case(s):
    vowels = 'aeiou'
    result =[]

    for ch in s:
        if ch == '-':
            result.append('_')
        elif ch.lower() in vowels:
            result.append(ch.lower())
        elif ch.isalpha():
            result.append(ch.upper())
        else:
            result.append(ch)

    return ''.join(result)
