import random

def main(n):
    # 生成测试数据
    # n: b 和 g 的长度
    # 约束：max(b) <= min(g)，避免原逻辑直接输出 -1
    if n < 2:
        n = 2

    # 先生成 b
    # 为了有一定随机性，b 在 [1, 100] 范围内生成
    b = [random.randint(1, 100) for _ in range(n)]
    b.sort()
    max_b = b[-1]

    # 再生成 g，保证 min(g) >= max(b)
    # 令 g 在 [max_b, max_b + 100] 范围内生成
    g = [random.randint(max_b, max_b + 100) for _ in range(n)]

    m = len(g)

    # 以下为原始逻辑
    if max(b) > min(g):
        print(-1)
        return

    b.sort()
    res = sum(g) + sum(b[:-1]) * m
    if b[-1] in g:
        print(res)
    else:
        print(res + b[-1] - b[-2])


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)