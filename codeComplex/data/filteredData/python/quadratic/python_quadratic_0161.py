import random


def main(n):
    # 生成测试数据：n, k, p
    # 约束：确保 1 <= p[i] <= 10^5，1 <= k <= 10^5
    max_value = max(1, min(10**5, n * 10))
    k = random.randint(1, min(10**5, max_value))
    p = [random.randint(1, max_value) for _ in range(n)]

    t = []
    g = {}
    for x in p:
        if x in g:
            t.append(g[x])
            continue
        kk = x - 1
        while True:
            if kk in g:
                if x - g[kk] < k:
                    ttt = g[kk]
                else:
                    ttt = kk + 1
                for i in range(kk + 1, x + 1):
                    g[i] = ttt
                t.append(g[x])
                break
            elif kk < 0 or x - kk == k:
                for i in range(kk + 1, x + 1):
                    g[i] = kk + 1
                t.append(g[x])
                break
            kk -= 1

    print('n =', n)
    print('k =', k)
    print('p =', ' '.join(str(v) for v in p))
    print('result =', ' '.join(str(x) for x in t))


if __name__ == '__main__':
    # 示例：调用 main(10)，规模 n 可按需修改
    main(10)