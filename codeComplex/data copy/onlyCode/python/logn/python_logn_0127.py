"""
http://codeforces.com/contest/287/problem/B
"""


def sum(num):
    # num -= 1
    return (num * (num + 1)) // 2


def sum_from_to(fromm, to):
    if fromm <= 1:
        return sum(to)
    return sum(to) - sum(fromm)


def min_splitters():
    start = 1
    end = k
    while start < end:
        mid = (start + end) // 2
        mid_val = sum_from_to(mid, k)
        if mid_val == n:
            return k - mid + 1
        elif mid_val > n:
            start = mid + 1
        else:
            end = mid
    return k - start + 1


n, k = (int(i) for i in input().split())
# no need for splitters
if n == 1:
    print(0)
# one splitter is enough
elif n <= k:
    print(1)
else:
    k -= 1
    n -= 1
    # splitters aren't enough
    if sum(k) < n:
        print(-1)
    else:
        print(min_splitters())
