def to_screaming_snake_case(variable_name):
    result =[]
    
    for i, ch in enumerate(variable_name):
        if ch.isupper() and i>0 and variable_name[i-1].islower():
            result.append('_')

        if ch =='_' or ch =='-':
            result.append('_')

        else:
            result.append(ch.upper())
    
    return ''.join(result)
