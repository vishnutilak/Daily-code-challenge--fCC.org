def daylight_hours(latitude):
    lats = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]
    hours = [24, 23, 21, 15, 13, 12, 12, 11, 10, 9, 6, 2, 0]

    left = 0
    right = len(lats) - 1

    # Handle boundaries early
    if latitude <= lats[0]:
        return hours[0]
    if latitude >= lats[-1]:
        return hours[-1]

    # Binary search to find closest position
    while left <= right:
        mid = (left + right) // 2

        if lats[mid] == latitude:
            return hours[mid]
        elif lats[mid] < latitude:
            left = mid + 1
        else:
            right = mid - 1

    # Now: right < left
    # right is index of smaller neighbor
    # left is index of larger neighbor
    if abs(latitude - lats[right]) <= abs(latitude - lats[left]):
        return hours[right]
    else:
        return hours[left]
