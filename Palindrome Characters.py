def palindrome_locator(s):
    l=0
    r= len(s)-1

    while l<r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return "none"

    if len(s)%2==0:
        return str(s[l]+s[r])
    return str(s[l])
