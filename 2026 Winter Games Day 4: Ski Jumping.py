def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    others = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    my_score = distance_points + style_points + wind_comp + k_point_bonus

    higher = 0
    for score in others:
        if score > my_score:
            higher += 1

    if higher == 0:
        return "Gold"
    elif higher == 1:
        return "Silver"
    elif higher == 2:
        return "Bronze"
    else:
        return "No Medal"
