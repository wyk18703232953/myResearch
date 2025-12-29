from math import ceil
import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # n 为题目中的 n
    # k 随机生成为 [1, 3n] 区间内的整数，避免除零
    if n <= 0:
        return 0

    k = random.randint(1, max(1, 3 * n))

    result = ceil((8 * n) / k) + ceil((5 * n) / k) + ceil((2 * n) / k)
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用：可在此修改规模 n
    main(10)