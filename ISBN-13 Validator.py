def is_valid_isbn_13(s):

    for ch in s:
        if not ch.isdigit() and ch!="-":
            return False
    
    without_hyph = s.replace("-", "")
    if len(without_hyph)!=13:
        return False
    
    total=0
    for i in range(13):
        if i%2==1:
            total+= 3*int(without_hyph[i])
        else:
            total+= int(without_hyph[i])
    
    return total%10==0
