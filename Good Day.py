def get_greeting(s):
    h,m = map(int, s.split(":"))
    time = (60*h)+m

    if 300<=time<=719:
        return "Good morning"
    if 720<=time<=1079:
        return "Good afternoon"
    if 1080<=time<=1319:
        return "Good evening"
    else:
        return "Good night"
