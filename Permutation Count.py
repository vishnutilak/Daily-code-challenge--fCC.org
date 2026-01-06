def count_permutations(s):
    n = len(s)

    # frequency count
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # compute n!
    numerator = 1
    for i in range(1, n + 1):
        numerator *= i

    # compute product of fi!
    denominator = 1
    for f in freq.values():
        fact = 1
        for i in range(1, f + 1):
            fact *= i
        denominator *= fact

    return numerator // denominator
