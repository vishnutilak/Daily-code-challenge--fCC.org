def vowel_case(s):
    result = []
    vowels = "aeiouAEIOU"

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
        else:
            result.append(ch)

    return "".join(result)
