import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里令 k 为 [1, 10*n] 范围内的随机整数
    if n <= 0:
        raise ValueError("n must be a positive integer")
    k = random.randint(1, 10 * n)

    # 原始逻辑：输出 ceil(k / n)
    result = k // n + (k % n != 0)
    print(result)


if __name__ == "__main__":
    # 示例：手动指定规模
    main(10)