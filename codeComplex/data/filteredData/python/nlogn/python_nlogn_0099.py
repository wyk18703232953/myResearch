import random

def main(n):
    # 生成测试数据
    # 将 n 作为数组 x 的长度
    p = 0  # 原代码中 p 未被使用，这里仅占位
    v = random.randint(1, n - 1)  # 保证 v-1 合法，v ∈ [1, n-1]

    # 生成长度为 n 的随机整数数组
    x = [random.randint(0, 10**9) for _ in range(n)]

    # 原始逻辑
    x.sort()
    result = x[v] - x[v - 1]
    print(result)

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)