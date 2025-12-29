import random

def main(n: int):
    # 依据规模 n 自动生成测试数据
    # n 表示第一个参数 n 的规模上界，其余参数与之同量级
    if n <= 0:
        return  # 或者根据需要处理无效规模

    # 生成 n, m, a, b
    N = random.randint(1, n)          # 原代码中的 n
    M = random.randint(1, max(1, n))  # 原代码中的 m，确保不为 0
    A = random.randint(1, max(1, n))  # 原代码中的 a
    B = random.randint(1, max(1, n))  # 原代码中的 b

    # 原逻辑
    if N % M != 0:
        mn = N // M * M
        mx = N // M * M + M
        result = min(((N - mn) * B), ((mx - N) * A))
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例：以 100 作为规模调用
    main(100)