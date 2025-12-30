import random

def main(n: int) -> int:
    # 生成测试数据
    # 约束：保证 m >= 1，k >= 0，a 为非负整数
    m = max(1, n // 3)        # 模数规模随 n 变化
    k = random.randint(0, 10) # 每步常数扣减
    a = [random.randint(0, 10) for _ in range(n)]

    # 原逻辑开始
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + m * a[i - 1] - k

    M = [10 ** 20] * m
    ans = 0
    for i in range(0, n + 1):
        M[i % m] = min(M[i % m], b[i])
        for j in range(0, m):
            if i > j:
                ans = max(ans, b[i] - M[j] - k * ((m * i + m - (i - j)) % m))
    result = ans // m

    # 为了便于在外部看到使用的数据和结果，可以按需打印
    # 这里仅返回结果；如需调试，可自行添加打印语句
    return result


if __name__ == "__main__":
    # 示例：调用 main(10)
    print(main(10))