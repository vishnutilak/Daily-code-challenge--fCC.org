def detect_roast(beans):
    n = len(beans)
    points =0

    for ch in beans:
        if ch=="'": points +=1
        if ch=="-": points +=2
        if ch==".": points +=3

    points /=n

    if points<1.75:
        return "Light"
    if 1.75<=points<=2.5:
        return "Medium"
    else:
        return "Dark"
