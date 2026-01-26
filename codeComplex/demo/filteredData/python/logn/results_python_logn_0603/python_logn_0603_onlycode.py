import sys
sys.setrecursionlimit(1000)


def estimate(a):
    return int(((n - a) * (n + 1 - a)) / 2) - a


def dicho(lower, upper, target):
    if estimate(lower) == target:
        return lower
    elif estimate(upper) == target:
        return upper
    else:
        mid = (int)((lower + upper) / 2)
        if(estimate(mid) < target):
            upper = mid
        else:
            lower = mid
        return dicho(lower, upper, target)


n, k = map(int, input().split())
lower = 0
upper = n
print(dicho(lower, upper, k))
