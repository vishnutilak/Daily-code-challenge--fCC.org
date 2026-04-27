def truncate_text(s):
    width=0
    res =""

    for ch in s:
        if width>=50: break

        elif ch in "ilI":
            width +=1
            res +=ch

        elif ch in "fjrt":
            width +=2
            res +=ch

        elif ch in "abcdeghkmnopqrstuvwxyzJL":
            width +=3
            res +=ch

        elif ch in "ABCDEFGHKMNOPQRSTUVWXYZ":
            width +=4
            res +=ch

        elif ch==" ":
            width +=2
            res +=ch
        
        elif ch==".":
            width +=1
            res +=ch
    
        else: res+=ch
    
    if width<=50: return res
    else: return res[:-2]+"..."
