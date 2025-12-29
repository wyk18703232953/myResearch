import math
import random

def main(n):
    # 根据 n 生成测试数据，这里示例：k 在 [0, n] 范围内随机生成
    k = random.randint(0, n)

    # 原始逻辑
    a = math.sqrt(1 + 2 * k + 2 * n) - 1
    result = n - int(a)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(100)，你可以自行修改 n 的大小
    main(100)