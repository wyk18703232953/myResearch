import random

def main(n):
    # 生成测试数据
    # complexity 为 n 个随机正整数
    complexity = [random.randint(1, 1000) for _ in range(n)]
    complexity.sort()

    # chores 第 3 个元素作为索引，需要是 [1, n-1] 之间的安全下标
    # 且在原题语义下，complexity[chores[2]] 与 complexity[chores[2]-1] 都要合法
    idx = random.randint(1, n - 1)  # 1 ~ n-1
    chores = [
        random.randint(0, n - 1),  # 随便生成，其实只用到 chores[2]
        random.randint(0, n - 1),
        idx
    ]

    # 原始逻辑
    result = complexity[chores[2]] - complexity[chores[2] - 1]
    print(result)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)