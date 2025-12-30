import random

def main(n):
    # 生成测试数据
    # a 为数组 A 的长度（至少 2），b 为查询次数
    a = max(2, n)          # 确保 a >= 2
    b = n                  # 这里简单设为 n 次查询

    # 生成 A：长度为 a 的随机整数序列
    A = [random.randint(1, 100) for _ in range(a)]

    # 原逻辑开始
    A.append(-1)
    B = []
    Z = []
    AN = []
    x, y = A[0], A[1]

    for i in range(a - 1):
        Z.append((x, y))
        if x > y:
            B.append(y)
            y = A[i + 2]
        else:
            B.append(x)
            x, y = y, A[i + 2]

    # 构造 b 个查询 w
    # 覆盖范围：1..len(Z)+len(B) 的一些值，保证既有 <=len(Z) 也有 >len(Z) 的情况
    max_query = len(Z) + len(B)
    if max_query == 0:
        queries = [1] * b
    else:
        queries = [random.randint(1, max_query) for _ in range(b)]

    for w in queries:
        if w <= len(Z):
            AN.append(Z[w - 1])
        else:
            # 注意：原程序这里有潜在除零，若 len(B)==0 且 w>len(Z) 会崩溃
            # 为保持语义一致，这里也保持相同行为，不做防护
            w_mod = w % len(B)
            AN.append((x, B[w_mod - 1]))

    for W in AN:
        print(*W)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)