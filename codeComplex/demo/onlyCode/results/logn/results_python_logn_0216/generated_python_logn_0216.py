import sys, math, queue, bisect
MOD = 10**9+7
sys.setrecursionlimit(1000000)

def main(n):
    global s
    s = n // 2
    def ok(x):
        y = sum(map(int, list(str(x))))
        return x - y >= s
    l, h = 0, n
    a = n
    while l <= h:
        m = (l + h) >> 1
        if ok(m):
            a = m - 1
            h = m - 1
        else:
            l = m + 1
    return n - a

if __name__ == "__main__":
    print(main(10**6))