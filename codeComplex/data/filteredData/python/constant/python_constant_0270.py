def main(n):
    # Deterministically generate x = [n, pos, l, r]
    # Interpret n as the total size/upper bound; derive other params from n
    total_n = max(1, n)
    pos = (n // 3) % total_n + 1
    l = (n // 5) % total_n + 1
    r = (n // 2) % total_n + 1
    if l > r:
        l, r = r, l

    x = [total_n, pos, l, r]

    pos = x[1]
    n_val = x[0]
    l = x[2]
    r = x[3]
    step = 0
    if pos < l:
        step = l - pos + 1
        if r < n_val:
            step += r - l + 1
    elif pos > r:
        step = pos - r + 1
        if l > 1:
            step += r - l + 1

    else:
        if l > 1 and n_val > r:
            step += min(pos - l, r - pos) + r - l + 2
        elif l == 1 and n_val > r:
            step = r - pos + 1
        elif l > 1 and n_val == r:
            step += pos - l + 1

        else:
            step = 0

    # print(step)
    pass
if __name__ == "__main__":
    main(10)