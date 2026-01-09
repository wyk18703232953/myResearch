def main(n):
    t = n if n > 0 else 1
    # Deterministically construct g of length t
    # Pattern: first increasing then decreasing with a single maximum at position t//2
    g = []
    peak_pos = t // 2
    for i in range(t):
        if i <= peak_pos:
            g.append(i)  # non-decreasing part

        else:
            g.append(peak_pos - (i - peak_pos))  # non-increasing part

    k = max(g)
    i = 0
    while g[i] != k:
        if i != 0 and g[i] < g[i - 1]:
            # print("NO")
            pass
            return
        i += 1
    i += 1
    while i < t and g[i] != k:
        if i != 0 and g[i] > g[i - 1]:
            # print("NO")
            pass
            return
        i += 1
    # print("YES")
    pass
if __name__ == "__main__":
    main(10)