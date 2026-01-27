def main(n):
    # n controls the number of bits used (like mp in original code)
    # To keep behavior reasonable, cap n at 29 (original mp)
    mp = min(max(n, 0), 29)

    # Precompute powers of two (length mp+1 is enough)
    powers = [1]
    for _ in range(32):
        powers.append(powers[-1] * 2)

    # Fixed hidden numbers a and b for deterministic behavior
    hidden_a = 3
    hidden_b = 1

    qqq = {'cnt': 0}  # to mimic global counter if needed

    def get_ans(c, d):
        qqq['cnt'] += 1
        # Simulate the interactive judge using XOR comparison with fixed a, b
        if (hidden_a ^ c) > (hidden_b ^ d):
            return -1
        elif (hidden_a ^ c) < (hidden_b ^ d):
            return 1
        return 0

    # Initialize algorithm variables
    a, b = 0, 0
    c, d = 0, 0

    q = get_ans(0, 0)

    for i in range(mp + 1):
        cp = mp - i
        c += powers[cp]
        d += powers[cp]
        if q == 0:
            continue
        t = get_ans(c, d)

        if t != q:
            if t == 1:
                a += powers[cp]
                c -= powers[cp]
            elif t == -1:
                b += powers[cp]
                d -= powers[cp]
            q = get_ans(c, d)

    for i in range(mp + 1):
        cp = mp - i
        if (c & powers[cp]) > 0 and (d & powers[cp]) > 0:
            c -= powers[cp]
            t = get_ans(c, d)

            if t < 0:
                a += powers[cp]
                b += powers[cp]

            c += powers[cp]

    # Return the discovered a, b and the number of calls for analysis
    return a, b, qqq['cnt']


if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    result = main(29)
    # print(result)
    pass