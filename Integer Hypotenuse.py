def is_integer_hypotenuse(a, b):
    s = a * a + b * b
    r = int(s ** 0.5)
    return r * r == s
