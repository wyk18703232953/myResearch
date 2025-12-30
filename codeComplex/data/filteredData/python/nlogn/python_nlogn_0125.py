import random

def main(n: int):
    # 生成测试数据
    # 约定：
    #   m：目标值，正整数
    #   k：初始值，非负整数，且 k < m（否则答案必为 0）
    #   line：长度为 n 的正整数数组
    #
    # 你可以根据需要修改生成策略，这里给出一个简单示例：
    m = max(1, n * 5)                 # 目标值随 n 线性增长
    k = random.randint(0, max(0, m-1))  # 初始值在 [0, m-1] 之间
    line = [random.randint(1, 10) for _ in range(n)]

    # 原始逻辑
    line.sort(reverse=True)
    count = 0
    if k >= m:
        print(count)
        return

    for i in range(n):
        k += line[i] - 1
        count += 1
        if k >= m:
            print(count)
            return

    print(-1)


if __name__ == "__main__":
    # 示例：运行若干不同规模
    for size in [5, 10, 20]:
        print(f"n = {size}: ", end="")
        main(size)