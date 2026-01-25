def main(n):
    # Deterministic generation of input structure
    # n is both the length of the list and (modulo pattern) controller of values
    if n <= 0:
        return

    # Example deterministic construction: l[i] cycles through 0..3 based on i
    l = [(i % 4) for i in range(n)]

    # Core algorithm from original code
    ll = []
    res = []
    head = 0
    dia = 0

    for i in range(1, n):
        if l[i] == 1:
            l[i] = 0
            ll.append(i)
        else:
            res.append((head + 1, i + 1))
            l[head] -= 1
            dia += 1
            head = i
            l[head] -= 1

    if l[head] > 0 and len(ll) > 0:
        res.append((ll[0] + 1, head + 1))
        l[head] -= 1
        del ll[0]
        dia += 1

    if l[0] > 0 and len(ll) > 0:
        res.append((ll[0] + 1, 1))
        l[0] -= 1
        del ll[0]
        dia += 1

    for i in ll:
        for j in range(n):
            if l[j] > 0:
                res.append((j + 1, i + 1))
                l[j] -= 1
                break

    if len(res) < n - 1:
        print("NO")
    else:
        print("YES " + str(dia))
        print(n - 1)
        for p in res:
            print(p[0], p[1])


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)