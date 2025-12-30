import random
import math

def resistors(a, b):
    ans = 0
    while b:
        ans += a // b
        a, b = b, a % b
    return ans

def main(n):
    # 生成两个不为零的随机正整数，规模与 n 相关
    # 这里简单设为 [1, n] 区间内
    if n < 1:
        n = 1
    a = random.randint(1, n)
    b = random.randint(1, n)
    # 确保不同时为 0（当前生成方式已保证）
    return resistors(a, b)

if __name__ == "__main__":
    # 示例：使用 n = 100 运行一次
    print(main(100))