def main(n):
    # n is the number of elements
    # Generate deterministic array for lst(): length n
    arr = [(i * 2 + 3) % (n + 7) for i in range(n)]
    # Generate deterministic string s of length 2*n with exactly n '0' and n '1'
    # Pattern: first n chars are '0', last n chars are '1'
    s = '0' * n + '1' * n

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