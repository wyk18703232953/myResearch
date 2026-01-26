def main(n):
    # Construct a deterministic string a of length n over 'b' and 'w'
    if n <= 0:
        # print(0)
        pass
        return
    # Example pattern: alternating 'b' and 'w'
    a = ''.join('b' if i % 2 == 0 else 'w' for i in range(n))

    n_len = len(a)
    b = []
    c = 0
    d = 0
    for i in range(1, n_len):
        if a[i] == a[i - 1]:
            b.append(['bw'.find(a[c]), i - c])
            d = max(d, i - c)
            c = i
    b.append(['bw'.find(a[c]), n_len - c])
    d = max(d, n_len - c)
    if d < n_len and b[0][0] == (b[-1][0] + b[-1][1]) % 2:
        d = max(d, b[-1][1] + b[0][1])
    # print(d)
    pass
if __name__ == "__main__":
    main(10)