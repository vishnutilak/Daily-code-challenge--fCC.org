def capitalize_fibonacci(s):
    result =[]
    s= s.lower()
    a,b =0,1
    fibs = [0,1]
    for i in range(len(s)):
        a,b= b, a+b
        fibs.append(b)
    
    for i in range(len(s)):
        if i in fibs:
            result.append(s[i].upper())
        else:
            result.append(s[i])
    return ''.join(result)
