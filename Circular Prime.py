def is_circular_prime(n: int) -> bool:

    if n < 10:
        return n in (2, 3, 5, 7)

    s = str(n)
    # Digit pruning 
    for c in s:
        if c in "024568":
            return False

    # Check all rotations
    for _ in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[1:] + s[0]

    return True


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True
