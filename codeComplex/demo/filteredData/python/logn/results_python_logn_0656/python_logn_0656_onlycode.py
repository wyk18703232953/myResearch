def func():
    n, k = map(int, input().strip().split())
    l = 0
    r = n
    while l <= r:
        mid = (l + r) // 2
        if mid*(mid+1)/2 - (n-mid) < k:
            l = mid + 1
        elif mid*(mid+1)/2 - (n-mid) > k:
            r = mid
        else:
            print(n - mid)
            return mid


if __name__ == '__main__':
    func()