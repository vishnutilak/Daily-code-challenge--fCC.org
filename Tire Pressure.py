def tire_status(pressures_psi, range_bar):

    result =[]
    minTP = range_bar[0]*14.5038
    maxTP = range_bar[1]*14.5038

    for tire in pressures_psi:
        if tire<minTP :
            result.append("Low")
        elif tire>maxTP:
            result.append("High")
        else:
            result.append("Good")

    return result
