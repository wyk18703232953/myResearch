import random

def main(n):
    # 生成测试数据：n 行，m 列
    # 可以根据需要修改 m 和生成策略
    m = 5
    # 生成 a 为 n x m 的矩阵，元素在 [0, 10^9] 范围内
    random.seed(0)
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    ok = 0
    ng = 10**9 + 1
    judge = (1 << m) - 1
    dg = 1000

    # 二分答案
    while ng - ok > 1:
        mid = (ng + ok) // 2
        tank = set()
        for i in range(n):
            r = 0
            for j in range(m):
                r <<= 1
                if a[i][j] >= mid:
                    r |= 1
            tank.add(r)

        updated = False
        for p in tank:
            # 小优化：只遍历 q >= p 也可以，但保持与原逻辑一致
            for q in tank:
                if p | q == judge:
                    ok = mid
                    updated = True
                    break
            if updated:
                break
        if not updated:
            ng = mid

    # 重新构造 tank 和 res
    tank = set()
    res = []
    for i in range(n):
        r = 0
        for j in range(m):
            r <<= 1
            if a[i][j] >= ok:
                r |= 1
        if r not in tank:
            res.append(i * dg + r)
        tank.add(r)

    # 输出满足条件的两个下标（1-based）
    for p in res:
        for q in res:
            if (p % dg) | (q % dg) == judge:
                print(p // dg + 1, q // dg + 1)
                return


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)