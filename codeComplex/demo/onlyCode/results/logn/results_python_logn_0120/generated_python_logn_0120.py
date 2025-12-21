def main(n):
    k = n
    if n == 1:
        return 0
    if n <= k:
        return 1
    lo, hi = 1, k - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        cum = (k - 2 + mid - 1) * (k - mid) // 2
        if cum < n - k:
            hi = mid - 1
        else:
            lo = mid
    if lo == 1:
        return -1
    return k - lo + 1

if __name__ == "__main__":
    print(main(10))