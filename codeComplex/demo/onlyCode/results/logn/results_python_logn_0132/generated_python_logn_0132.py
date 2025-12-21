def main(n):
    k = n
    if n == 1:
        return 0
    if n - 1 > (1 + k - 1) * (k - 1) // 2:
        return -1
    n -= 1
    k -= 1
    l, r = 0, k + 1
    while r - l > 1:
        m = (l + r) // 2
        if (m + k) * (k - m + 1) // 2 >= n:
            l = m
        else:
            r = m
    return k - l + 1

if __name__ == "__main__":
    print(main(10))