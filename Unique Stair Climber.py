def get_unique_climbs(steps):
    if steps==1: return 1
    if steps==2: return 2

    once,twice = 1, 2

    for _ in range(3, steps+1):
        thrice = once +twice
        once = twice
        twice = thrice

    return twice
