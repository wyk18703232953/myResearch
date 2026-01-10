from collections import defaultdict as di

def main(n):
    a = [(i * 3) % (n // 2 + 1) for i in range(n)]
    d = di(int)
    res, s = 0, 0
    for i in range(n):
        res += a[i] * i - s - d[a[i] - 1] + d[a[i] + 1]
        s += a[i]
        d[a[i]] += 1
    print(res)

if __name__ == "__main__":
    main(10)