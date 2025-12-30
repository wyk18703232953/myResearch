import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 令 s 为 [1, n^2] 的随机整数，且保证 n >= 1
    if n <= 0:
        raise ValueError("n must be positive")
    s = random.randint(1, n * n)

    # 原逻辑：输出 (s + n - 1) // n
    result = (s + n - 1) // n
    print(result)

# 示例：直接运行本文件时，给一个默认规模
if __name__ == "__main__":
    main(10)