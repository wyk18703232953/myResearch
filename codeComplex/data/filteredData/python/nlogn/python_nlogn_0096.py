import random

def main(n):
    # 生成测试数据
    # complexity 为长度至少要大于最大可能的 chores[2] 的数组
    # 这里设成 n 个不同的随机整数
    complexity = random.sample(range(1, 10 * n + 1), n)
    complexity.sort()

    # 生成 chores 数组，长度为 3，第三个元素为有效下标（1 ~ n-1）
    idx = random.randint(1, n - 1)
    chores = [
        random.randint(0, n - 1),
        random.randint(0, n - 1),
        idx
    ]

    # 原逻辑
    result = complexity[chores[2]] - complexity[chores[2] - 1]
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)