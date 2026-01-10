def speed_check(speed_mph, speed_limit_kph):
    
    kmph = 1.60934*speed_mph
  
    if kmph <= speed_limit_kph:
        return "Not Speeding"
    elif kmph <= speed_limit_kph + 5:
        return "Warning"
    else:
        return "Ticket"
