def get_initials(name):
    parts = name.split(" ")
    res =[]
    for part in parts:
        res.append(part[0].upper())
        res.append('.')
    
    return ''.join(res)
