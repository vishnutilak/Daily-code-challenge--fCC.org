def is_valid_equation(eq):
    left, right = eq.split('=')
    right = int(right.strip())
    
    tokens = left.strip().split()
    
    # Step 1: handle * and /
    stack = [int(tokens[0])]
    i = 1
    
    while i < len(tokens):
        op = tokens[i]
        num = int(tokens[i + 1])
        
        if op == '*':
            stack[-1] *= num
        elif op == '/':
            stack[-1] /= num
        else:
            stack.append(op)
            stack.append(num)
        
        i += 2
    
    # Step 2: handle + and -
    result = stack[0]
    i = 1
    
    while i < len(stack):
        op = stack[i]
        num = stack[i + 1]
        
        if op == '+':
            result += num
        else:
            result -= num
        
        i += 2
    
    return result == right
