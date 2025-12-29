from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 约定：s 为 1 到 10*n 之间的随机整数（可按需调整）
    if n <= 0:
        raise ValueError("n must be a positive integer")

    s = random.randint(1, 10 * n)

    # 原逻辑：输出 (s + n - 1) // n
    result = (s + n - 1) // n
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时由外部指定 n
    main(10)