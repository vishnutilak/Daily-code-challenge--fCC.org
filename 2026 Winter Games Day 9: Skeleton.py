def get_difficulty(track):

    points =0
    prev = None

    for ch in track:
        if ch=="L" :
            if prev =="R":
                points +=15
            else:
                points+=5

        elif ch=="R":
            if prev =="L":
                points +=15
            else:
                points+=5
        prev = ch
    
    if points<=100:
        return "Easy"
    elif points<=200:
        return "Medium"
    else:
        return "Hard"
