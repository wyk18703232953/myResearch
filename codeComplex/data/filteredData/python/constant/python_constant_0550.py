from math import ceil
import random

def main(n):
    # 生成测试数据：k 和 n
    # 约束：1 <= k <= n
    k = random.randint(1, n)
    total = n

    # 原逻辑：ceil(n / k)
    result = ceil(total / k)

    # 输出结果
    print(result)

if __name__ == "__main__":
    # 示例：规模为 100 时调用 main(100)
    main(100)