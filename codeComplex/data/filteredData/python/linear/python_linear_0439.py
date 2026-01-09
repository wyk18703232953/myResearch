import math

def getx(n):
    return math.floor(math.sqrt(n))

def getans(n, x):
    l1 = [i for i in range(n, 0, -1)]
    l2 = []
    i = 0
    while i < n:
        l2 = l2 + sorted(l1[i:i + x])
        i += x
    return l2

def main(n):
    if n <= 0:
        return []
    a = getx(n)
    ans = getans(n, a)
    ans1 = [str(i) for i in ans]
    # print(' '.join(ans1))
    pass
    return ans

if __name__ == "__main__":
    main(10)