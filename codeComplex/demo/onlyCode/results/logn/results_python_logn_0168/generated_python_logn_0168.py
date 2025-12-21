def prod(n):
    if n % 2:
        return n * ((n + 1) // 2)
    else:
        return (n // 2) * (n + 1)

def total_count(n, k):
    if k >= n:
        return (0, 0, 1)
    else:
        count = 0
        l = 1
        r = k
        s = prod(k)
        while l <= r:
            mid = (l + r) // 2
            if n > s - prod(mid) + mid:
                r = mid - 1
            else:
                l = mid + 1
        n = n - (s - prod(l) + l)
        count += (k - l + 1)
        k = l - 1
        return (n, k, count)

def main(n):
    k = n
    if prod(k) - (k - 1) < n:
        return -1
    elif n == 1:
        return 0
    elif k >= n:
        return 1
    else:
        n = n - k
        k = k - 2
        (n, k, count) = total_count(n, k)
        if n:
            return count + 2
        else:
            return count + 1

if __name__ == "__main__":
    for i in range(1, 11):
        print(i, main(i))