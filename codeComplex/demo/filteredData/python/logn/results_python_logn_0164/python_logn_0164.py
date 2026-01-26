def getSum(p, q):
    n = q - p + 1
    temp = (n * (p + q) // 2) - n + 1
    return temp, n


def main(n):
    # Interpret n as k, and derive target sum N deterministically from k
    k = max(2, n)
    target_n = k * (k + 1) // 2  # deterministic function of k

    l = 2
    r = k
    ans = -1

    while l <= r:
        mid = l + (r - l) // 2
        tot, count = getSum(mid, k)
        if tot >= target_n:
            ans = count
        if tot < target_n:
            r = mid - 1

        else:
            l = mid + 1
    if target_n == 1:
        ans = 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)