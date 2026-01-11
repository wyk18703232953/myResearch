def main(n):
    # Generate deterministic inputs based on n
    # Original expects:
    #   n: integer
    #   list of n integers
    #   s: string of length 2*n of '0'/'1'
    #
    # Here:
    #   - array: [n, n-1, ..., 1]
    #   - s: first n chars '0', next n chars '1'
    arr = [n - i for i in range(n)]
    s = "0" * n + "1" * n

    # Core algorithm (unchanged logic, without stdin/input)
    l = sorted(zip(arr, range(n)))
    p = 0
    ans = [0] * (2 * n)
    st = [0] * n
    ln = 0
    for i in range(2 * n):
        ch = s[i]
        if ch == '0':
            st[ln] = p
            ans[i] = l[p][1] + 1
            ln += 1
            p += 1

        else:
            ans[i] = l[st[ln - 1]][1] + 1
            ln -= 1

    # print(*ans)
    pass
if __name__ == "__main__":
    main(5)