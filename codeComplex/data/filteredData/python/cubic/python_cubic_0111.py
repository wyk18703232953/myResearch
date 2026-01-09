from collections import defaultdict

def main(n):
    # Deterministically generate input of size n
    # a[i] = (i % 10) - 5 yields values in range [-5, 4]
    a = [(i % 10) - 5 for i in range(n)]

    rec = defaultdict(list)
    for j in range(n):
        s = 0
        for k in range(j, n):
            s += a[k]
            rec[s].append((j, k))

    ans = []
    for key in rec.keys():
        tmp = []
        rec[key] = sorted(rec[key], key=lambda x: x[1])
        pre = -1
        for x, y in rec[key]:
            if pre >= x:
                continue
            tmp.append((x + 1, y + 1))
            pre = y
        if len(tmp) > len(ans):
            ans = tmp

    # print(len(ans))
    pass
    for x, y in ans:
        # print(x, y)
        pass
if __name__ == "__main__":
    main(10)