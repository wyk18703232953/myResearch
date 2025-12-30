from math import ceil
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 约束：1 <= k <= n*10，且 k > 0
    if n <= 0:
        return 0

    k = random.randint(1, max(1, n * 10))

    result = ceil(n * 2 / k) + ceil(n * 5 / k) + ceil(n * 8 / k)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)