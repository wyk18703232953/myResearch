def binary_search(n, k):
    left = -1
    right = n
    while left < right - 1:
        middle = (left + right) // 2
        if middle % 2 != 0:
            s = (1 + middle) * (middle // 2) + ((1 + middle) // 2)
        else:
            s = (1 + middle) * (middle // 2)
        if s - (n - middle) >= k:
            right = middle
        else:
            left = middle
    return right


n, k = map(int, input().split())
i = 1
count = 0
print(n - binary_search(n, k))