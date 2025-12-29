import random

def main(n: int):
    # 生成测试数据：
    # n 为 x 的长度，m 为 y 的长度（此处简单设为 n//2，至少为 1）
    if n <= 0:
        return

    m = max(1, n // 2)

    # 生成不重复的 x，范围为 [1, 10*n]
    x = random.sample(range(1, 10 * n + 1), n)

    # 从 x 中随机选出部分元素作为 y（保证一定有匹配）
    y = random.sample(x, m)

    # 原逻辑：在 x 中按 y 的值查找相等元素的下标，收集后按下标排序，再输出对应的元素
    indices = []
    for i in range(m):
        for j in range(n):
            if y[i] == x[j]:
                indices.append(j)

    result = ' '.join(map(str, [x[i] for i in sorted(indices)]))
    print(result)


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)