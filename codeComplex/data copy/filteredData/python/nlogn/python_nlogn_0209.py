def fun(k, li, t):
    tem = []
    count = 0
    for i in li:
        if i[0] >= k:
            tem.append(i)
            count += 1
    if count >= k:
        ans = 0
        for i in range(k):
            ans += tem[i][1]
        if ans <= t:
            return True

        else:
            return False

    else:
        return False

def main(n):
    # Deterministically generate n and t
    # Let actual_n = n, and t grow roughly as n^2 to allow some feasible solutions
    actual_n = n
    t = n * n

    # Generate li with structure similar to original:
    # li[i][0] = a_i (capability), li[i][1] = b_i (cost), li[i][2] = index
    # Use simple arithmetic patterns to ensure determinism
    li = []
    for i in range(actual_n):
        a = (i % (n + 1)) + 1          # capabilities between 1 and n+1
        b = (i * 2 + 3) % (2 * n + 5)  # costs in a fixed range
        li.append([a, b, i])

    li.sort(key=lambda x: x[1])

    l = 0
    r = actual_n
    while r - l > 1:
        mid = (l + r) // 2
        if fun(mid, li, t):
            l = mid

        else:
            r = mid

    fin = 0
    for i in range(l, r + 1):
        if fun(i, li, t):
            fin = i
    # print(fin)
    pass
    # print(fin)
    pass
    tem = []
    for i in range(actual_n):
        if li[i][0] >= fin:
            tem.append(li[i][2] + 1)
    # print(*tem[:fin])
    pass
if __name__ == "__main__":
    main(10)