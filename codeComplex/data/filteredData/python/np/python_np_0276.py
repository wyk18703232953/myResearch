import random

def solve(n, m, ops):
    h = m & -m
    for c in ops:
        if c == 'U' and m != (n + 1) >> 1:
            m += -h if (m + h) % (h << 2) == 0 else h
            h <<= 1
        if c in 'LR' and h > 1:
            h >>= 1
            m += -h if c == 'L' else h
    return m

def main(n):
    # 生成测试数据：
    # 1. 随机选择查询次数 q（规模与 n 同量级）
    # 2. 每个查询随机生成初始位置 m 和操作串 ops
    #
    # 注意：原题中 n 是完全二叉树节点数，要求通常是奇数，
    # 这里简单生成一个不大于 n 的奇数作为 n 的实际使用值。
    if n < 1:
        return

    if n % 2 == 0:
        n -= 1
        if n < 1:
            n = 1

    # 查询个数
    q = max(1, min(n, 10))  # 控制输出规模，最多 10 个查询

    results = []
    for _ in range(q):
        # 随机生成 m：1..n 之间的奇数
        m_candidates = [x for x in range(1, n + 1, 2)]
        m = random.choice(m_candidates)

        # 随机生成操作串长度和内容
        L = random.randint(0, 20)  # 操作长度控制在 0~20
        ops = ''.join(random.choice('ULR') for _ in range(L))

        ans = solve(n, m, ops)
        results.append(ans)

    # 输出结果
    for v in results:
        print(v)

if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行调整
    main(15)