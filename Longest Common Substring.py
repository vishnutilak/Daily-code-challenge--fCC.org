def get_longest_substring(s):
    n = len(s)
    

    for length in range(n-1, 0, -1):
        seen = set()
        for i in range(n-length+1):
            substring = s[i:i+length]

            if substring in seen:
                return substring
            seen.add(substring)


    return ""
