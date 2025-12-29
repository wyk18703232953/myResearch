import random

def main(n: int):
    # 1. 生成 n, m, k
    # 这里将 n 作为数组长度，其它参数根据 n 随机生成
    m = random.randint(1, max(1, 2 * n))          # 目标值
    k = random.randint(0, m)                     # 初始 k，不大于 m

    # 2. 生成长度为 n 的数组 a
    # 数组元素为正整数，范围可根据需要调整
    a1 = [random.randint(1, 10) for _ in range(n)]

    # 3. 按原逻辑处理
    a1 = sorted(a1)
    count = 0

    while a1 and k < m:
        k += a1.pop() - 1
        count += 1

    if k >= m:
        print(count)
    else:
        print("-1")


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)