def ballbuster5000(arr, rj):
    for i in arr:
        rj += i
    gg = 0
    i = 0
    while gg <= rj:
        gg += arr[i]
        rj -= arr[i]
        i -= -1
    return i


n = int(input())
x = list(map(int, input().strip().split()))
x.sort(reverse=True)
print(ballbuster5000(x, 0))