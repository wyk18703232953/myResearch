def lower_bound(n, k):
    low = 1
    high = k
    while low < high:
        mid = low + (high - low) // 2
        pipes = mid * k - (mid + 2) * (mid - 1) // 2
        if pipes >= n:
            high = mid
        else:
            low = mid + 1
    return low


def main():
    n, k = map(int, input().split())
    if n == 1:
        print(0)
    else:
        ans = lower_bound(n, k)
        if ans == k:
            print(-1)
        else:
            print(ans)


if __name__ == "__main__":
    main()