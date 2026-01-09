def main(n):
    a = n
    l = []
    total = 0

    # Deterministic data generation replacing input-based lines
    # Generate 4 lines, each of length a*a, using a simple deterministic pattern
    for i in range(4):
        line_chars = []
        for j in range(a * a):
            if i % 2 == 0:
                # Even-indexed line: alternate "0" and "1"
                line_chars.append('1' if (j + i) % 2 else '0')

            else:
                # Odd-indexed line: periodic pattern including '2'
                v = (j + i) % 3
                if v == 0:
                    line_chars.append('0')
                elif v == 1:
                    line_chars.append('1')

                else:
                    line_chars.append('2')
        line = ''.join(line_chars)
        l.append(line)

    # Keep original sorting logic
    l = sorted(
        l,
        key=lambda s: s[0::2].count('1') + s[1::2].count('0')
    )[::-1]

    # Keep original accumulation logic
    for z, v in enumerate(l):
        if z < 2:
            for i in range(a * a):
                total += (v[i] != '0') if i % 2 else (v[i] != '1')

        else:
            for i in range(a * a):
                total += (v[i] != '1') if i % 2 else (v[i] != '0')

    # print(total)
    pass
if __name__ == "__main__":
    main(10)