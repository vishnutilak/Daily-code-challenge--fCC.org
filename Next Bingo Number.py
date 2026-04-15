def get_next_bingo_number(n):
    num = int(n[1:])
    num = num+1 if num<75 else 1
    
    if num<=15:
        letter = 'B'
    elif num<=30:
        letter = 'I'
    elif num<=45:
        letter = 'N'
    elif num<=60:
        letter = 'G'
    elif num<=75:
        letter = 'O'
    
    return letter +str(num)
