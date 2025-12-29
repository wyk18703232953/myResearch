import random

def main(n: int):
    # 生成测试数据
    # n: 数组长度
    # m: 目标值，取一个与 n 同数量级的值
    # k: 初始值，随机生成，不超过 m
    a = [random.randint(1, 10) for _ in range(n)]
    m = random.randint(max(1, n // 2), max(1, n * 2))
    k = random.randint(0, m)

    # 原逻辑开始
    a.sort(reverse=True)
    i = 0
    while k < m and i < n:
        k += a[i] - 1
        i += 1
    result = i if k >= m else -1

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模自行设定
    main(10)