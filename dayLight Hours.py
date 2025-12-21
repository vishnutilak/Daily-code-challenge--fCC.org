def daylight_hours(latitude):
    table = {
        -90: 24,
        -75: 23,
        -60: 21,
        -45: 15,
        -30: 13,
        -15: 12,
          0: 12,
         15: 11,
         30: 10,
         45: 9,
         60: 6,
         75: 2,
         90: 0
    }
    #lat:dayLightH

    closest_lat = 0
    smallest_diff = float('inf')
##finding the nearest value from the given input
    for lat in table:
        diff = abs(latitude - lat)
        if diff < smallest_diff:
            smallest_diff = diff
            closest_lat = lat

    return table[closest_lat]
