def main(n):
    a = max(1, n)
    l = []
    total = 0

    # Generate 4 deterministic strings of length a*a
    for i in range(4):
        base = []
        for j in range(a * a):
            # Deterministic pattern depending on i and j
            bit = ((i + j) % 2)
            base.append(str(bit))
        line = "".join(base)
        l.append(line)

    l = sorted(
        l,
        key=lambda s: s[0::2].count('1') + s[1::2].count('0')
    )[::-1]

    for z, v in enumerate(l):
        if z < 2:
            for i in range(a * a):
                total += (v[i] != '0') if i % 2 else (v[i] != '1')
        else:
            for i in range(a * a):
                total += (v[i] != '1') if i % 2 else (v[i] != '0')
    print(total)


if __name__ == "__main__":
    main(3)