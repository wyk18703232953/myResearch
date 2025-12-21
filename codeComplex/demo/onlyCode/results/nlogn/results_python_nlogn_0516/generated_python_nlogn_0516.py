def main(n):
    from collections import defaultdict as dd
    res = []
    for _ in range(n):
        m = max(4, n)
        l = [i % (n // 2 + 1) for i in range(m)]
        l1 = dd(int)
        a = 0
        for j in l:
            l1[j] += 1
            if l1[j] == 4:
                a = j
        if a:
            res.append((a, a, a, a))
        else:
            c = 0
            x = 0
            l2 = []
            for j in l1:
                if l1[j] >= 2:
                    l2.append(j)
            l2.sort()
            b = 0
            for j in l2:
                c += 1
                if c == 1:
                    a = j
                elif c == 2:
                    b = j
                else:
                    if x / j + j / x < a / b + b / a:
                        a, b = x, j
                x = j
            res.append((a, a, b, b))
    return res

if __name__ == "__main__":
    print(main(5))