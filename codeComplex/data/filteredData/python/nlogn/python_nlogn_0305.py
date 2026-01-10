def main(n):
    # Generate deterministic weights: a simple permutation of 1..n
    # Example: w[i] = (i*2 + 3) % n + 1 ensures values in [1, n] and mostly distinct
    w = [((i * 2 + 3) % n) + 1 for i in range(n)]

    # Generate deterministic ent string of length 2*n with exactly n '0' and n '1'
    # Pattern: alternating "01" ensures valid stack behavior
    ent = []
    for i in range(n):
        ent.append('0')
        ent.append('1')
    ent = ''.join(ent)

    mp = {w[i]: i + 1 for i in range(n)}
    sorted(mp)
    w.sort()
    ptr = 0
    stk = []
    out = []
    for i in range(2 * n):
        if ent[i] == "0":
            out.append(str(mp[w[ptr]]))
            stk.append(mp[w[ptr]])
            ptr += 1
        else:
            out.append(str(stk.pop()))
    print(" ".join(out))


if __name__ == "__main__":
    main(5)