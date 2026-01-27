def main(n):
    # Deterministically generate n, pos, l, r from input scale n
    # Ensure 1 <= l <= pos <= r <= n and segment length not always full
    if n < 4:
        n_val = 4

    else:
        n_val = n
    pos = (n_val // 2) + 1
    if pos > n_val:
        pos = n_val
    l = max(1, pos - (n_val // 4))
    r = min(n_val, pos + (n_val // 4))
    if r == l:
        if r < n_val:
            r = l + 1
        elif l > 1:
            l = r - 1
    if r - l + 1 == n_val:
        if r > l + 1:
            r -= 1

        else:
            if l > 1:
                l -= 1

            else:
                r = n_val - 1
    n, pos = n_val, pos

    if (r - l + 1) == n:
        # print(0)
        pass
        return
    if pos > l and pos < r:
        if n > r and l > 1:
            x = pos - l + 1 + r - l + 1
            y = r - pos + 1 + r - l + 1
            ans = min(x, y)

        else:
            if n == r:
                ans = pos - l + 1
            elif l == 1:
                ans = r - pos + 1
    elif pos >= r:
        if n > r:
            ans = pos - r + 1

        else:
            ans = 0
        if l > 1:
            ans += r - l + 1
    elif pos <= l:
        if l > 1:
            ans = l - pos + 1

        else:
            ans = 0
        if n > r:
            ans += r - l + 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)