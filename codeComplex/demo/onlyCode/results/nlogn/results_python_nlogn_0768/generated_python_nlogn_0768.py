def main(n):
    import math
    import sys
    import collections

    def getdict(x):
        d = {}
        if type(x) is list:
            for i in x:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        else:
            for i in range(x):
                t = i
                if t in d:
                    d[t] += 1
                else:
                    d[t] = 1
        return d

    def cdiv(a, k):
        return a // k + (a % k != 0)

    res = []
    t = n
    for _ in range(t):
        cur_n = n
        d = list(range(1, cur_n + 1))
        d.sort()
        if cur_n >= 2:
            res.append(min(d[-2] - 1, cur_n - 2))
        else:
            res.append(0)
    return res

if __name__ == "__main__":
    print(main(5))