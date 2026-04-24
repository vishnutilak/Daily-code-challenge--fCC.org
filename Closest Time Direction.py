def get_direction(time1, time2):

    h1,m1 = map (int, time1.split(":"))
    h2,m2 = map (int, time2.split(":"))
    
    t1 = (h1*60)+m1
    t2 = (h2*60)+m2

    day = 24*60

    positive = (t2-t1)%day
    negative = (t1-t2)%day

    if negative < positive:
        return "backward"
    if positive < negative :
        return "forward"
    else:
        return "equal"
