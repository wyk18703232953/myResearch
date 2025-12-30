import random

def main(n):
    # 生成测试数据：构造一个测试用例
    # t 为测试用例个数，这里固定为 1
    t = 1

    # 这里令 m 与 n 相同，也可以修改为其它规则，例如 m = max(1, n // 2) 等
    m = n

    # 随机生成一个 n x m 的棋盘，数值范围可根据需要调整
    # 为了可重复性，可以固定随机种子；若不需要可删除下一行
    random.seed(0)

    test_cases = []
    for _ in range(t):
        board = [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]
        test_cases.append((n, m, board))

    # 原算法逻辑
    for n, m, board in test_cases:
        l = []
        for i in range(n):
            li = board[i]
            for j in range(m):
                l.append((li[j], j))

        l.sort(key=lambda x: x[0], reverse=True)
        idxs = set()
        z = 0
        while len(idxs) < min(n, m) and z < len(l):
            curr = l[z]
            idxs.add(curr[1])
            z += 1

        idxs = list(idxs)
        total = 0

        # 对所有 n^n 种旋转方案枚举
        for i in range(n ** n):
            rotations = []
            num = i
            for j in range(n - 1, -1, -1):
                nj = n ** j
                q = num // nj
                num -= q * nj
                rotations.append(q)

            subtotal = 0
            for k in range(n):
                subtotal += max(
                    board[(k + rotations[col]) % n][idxs[col]]
                    for col in range(min(n, m))
                )
            total = max(total, subtotal)

        print(total)


# 示例调用
if __name__ == "__main__":
    # 例如 n = 3；注意原算法是 O(n^n * n^2)，n 大时会非常慢
    main(3)