def alarm_check(alarm_time, wake_time):
    h1, m1 = map(int, alarm_time.split(":"))
    h2, m2 = map(int, wake_time.split(":"))

    alarm = (h1*60)+m1
    wakey = (h2*60)+m2

    if 0<=wakey-alarm<=10:
        return "on time"
    elif wakey-alarm <0:
        return "early"
    else:
        return "late"
