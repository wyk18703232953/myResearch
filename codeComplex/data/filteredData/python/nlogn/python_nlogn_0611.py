def main(n):
    from bisect import bisect_left

    # Deterministic generation of c_tv, c_es based on n
    c_tv = n + 5
    c_es = (n % 7) + 1  # ensure >0

    # Deterministic intervals generation
    start = []
    end = []
    add = 0
    for i in range(n):
        l = i * 2
        r = l + (i % 5) + 1
        add += (r - l)
        start.append(l)
        end.append(r)

    start.sort()
    end.sort()

    ans = add * c_es + n * c_tv
    M = 10**9 + 7
    v = [0] * (n + 1)

    for i in range(n):
        indx = bisect_left(end, start[i]) - 1
        k = indx
        while k >= 0 and (start[i] - end[k]) * c_es < c_tv and v[k] == 1:
            k -= 1
        if k == -1:
            continue
        if (start[i] - end[k]) * c_es < c_tv:
            ans -= c_tv - (start[i] - end[k]) * c_es
            v[k] = 1

    print(ans % M)


if __name__ == "__main__":
    main(10)