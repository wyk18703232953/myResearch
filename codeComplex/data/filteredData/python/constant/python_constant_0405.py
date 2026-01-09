def main(n):
    # Deterministically generate two equal-length strings of length n
    # using only '0' and 'X', patterned by index parity
    s1 = ''.join('0' if i % 2 == 0 else 'X' for i in range(n))
    s2 = ''.join('X' if i % 3 == 0 else '0' for i in range(n))

    l, r = [{'0': 1, 'X': 0}[c] for cc in zip(s1, s2) for c in cc], 0
    for i in range(0, len(l) - 3, 2):
        s = 7 - sum(l[i:i + 4])
        if s < 5:
            r += 1
            l[i:i + s] = [0] * s
    # print(r)
    pass
if __name__ == "__main__":
    main(1000)