def get_bingo_letter(n):
    if n>=1 and n<=15:
        return "B"
    if n>=16 and n<=30:
        return "I"
    if n>=31 and n<=45:
        return "N"
    if n>=46 and n<=60:
        return "G"
    if n>=61 and n<=75:
        return "O"
    else:
        return n
