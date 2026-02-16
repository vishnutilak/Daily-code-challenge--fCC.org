def get_fastest_speed(times):
    segments = [320, 280, 350, 300, 250]
    fast_speed = 0.0
    lap = 0
    for i in range(5):
        speed = segments[i]/times[i]
        if speed >fast_speed:
            fast_speed = speed
            lap = i+1
    
    speed_str = format(fast_speed, ".2f")

    return "The luger's fastest speed was "+ speed_str+ " m/s on segment "+ str(lap) +"."
