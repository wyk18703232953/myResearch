def solve():
    n, k = [int(x) for x in input().split(' ')]
    t = input()
    j = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            j = i
    s = t + (k - 1) * t[-(n - j):]
    return s

print(solve())

