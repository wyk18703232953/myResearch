from sys import stdin


def quadratic(a, b, c):
    num = (b * b) - (4 * a * c)
    if num >= 0:
        return [(-b + (num ** .5)) / (2.0 * a), (-b - (num ** .5)) / (2.0 * a)]
    else:
        return [.5, .5]


n, k = map(int, stdin.readline().split())
for root in quadratic(1, 3, -2 * n - 2 * k):
    ans = n - root
    if ans > -1:
        print(int(ans))
        exit()
