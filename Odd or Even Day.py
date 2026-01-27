import datetime

def odd_or_even_day(timestamp):
    dateOnly = datetime.datetime.utcfromtimestamp(timestamp/1000)


    return "even" if dateOnly.day%2==0 else "odd"
