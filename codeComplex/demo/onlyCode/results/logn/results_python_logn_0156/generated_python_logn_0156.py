def reach_max(n, k):
    return n * k + 1 - n * (n + 1) // 2

def main(n):
    k = max(2, n * 2)
    if n == 1:
        return 0
    lo, hi = 1, k - 1
    if n > reach_max(hi, k):
        return -1
    while lo < hi:
        mid = (lo + hi) // 2
        if reach_max(mid, k) < n:
            lo = mid + 1
        else:
            hi = mid
    return lo

if __name__ == "__main__":
    print(main(10))