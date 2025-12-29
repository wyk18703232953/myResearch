import random

def getsum(N: int) -> int:
    A = (N + 1) // 2
    r1 = -A + A * (A + 1)
    B = N // 2
    r2 = B * (B + 1)
    return -r1 + r2

def main(n: int):
    """
    n: 规模，表示要生成的区间查询数量 Q
    自动生成 Q 对 (L, R) 区间，并输出对应结果。
    """
    Q = n

    # 为了可重复性，可以固定随机种子（如不需要可删除下一行）
    random.seed(0)

    # 生成测试数据：Q 组 (L, R)
    # 设定数轴上限为 10^6 * n（可以根据需要调整）
    max_val = max(1, 10**6 * n)
    queries = []
    for _ in range(Q):
        L = random.randint(1, max_val)
        R = random.randint(L, max_val)  # 保证 L <= R
        queries.append((L, R))

    # 处理并输出结果
    for L, R in queries:
        result = getsum(R) - getsum(L - 1)
        print(result)

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)