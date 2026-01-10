def main(n):
    # Deterministically generate input array ns of length n
    # Example pattern: ns[i] = i // 2 to allow duplicates and growth with n
    ns = [i // 2 for i in range(n)]

    a = 'cslnb'
    b = 'sjfnb'
    ns.sort()
    ans = []
    for i in range(1, n):
        if ns[i] == ns[i - 1]:
            ans.append(i)
    if len(ans) >= 2 or sum(ns) == 0:
        print(a)
        return
    if len(ans) == 1:
        i = ans[0]
        if ns[i] == 0 or ns[i] - 1 in ns:
            print(a)
            return
        r = sum(ns) - n * (n - 1) // 2
        if r % 2 == 0:
            print(a)
            return
        else:
            print(b)
            return
    else:
        r = sum(ns) - n * (n - 1) // 2
        if r % 2 == 0:
            print(a)
            return
        else:
            print(b)


if __name__ == "__main__":
    main(10)