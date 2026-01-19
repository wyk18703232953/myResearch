import math

mod = int(1e9) + 7
INF = float('inf')

def main(n):
    if n <= 0:
        print(-1)
        return

    # 生成确定性输入数据：
    # l[i] = i + 2  （从 2 开始递增）
    # c[i] = (i % 5) + 1  （周期性成本）
    l = [i + 2 for i in range(n)]
    c = [(i % 5) + 1 for i in range(n)]

    d = {}
    for i in range(n):
        x = l[i]
        cost = c[i]
        if x in d:
            d[x] = min(d[x], cost)
        else:
            d[x] = cost

    for i in l:
        lis = list(d.keys())
        for j in lis:
            g = math.gcd(i, j)
            new_cost = d[i] + d[j]
            if g in d:
                if new_cost < d[g]:
                    d[g] = new_cost
            else:
                d[g] = new_cost

    if 1 in d:
        print(d[1])
    else:
        print(-1)


if __name__ == "__main__":
    main(10)