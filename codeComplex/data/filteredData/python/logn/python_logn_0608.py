import math
import random

def main(n):
    # 根据 n 生成测试数据
    # 假设 k 的规模与 n 同级，这里生成随机 k，使得公式内根号合法
    # 原式中有 sqrt(9 + 8*(k+n))，需要保证 9 + 8*(k+n) >= 0
    # 对于 n 为正整数，这里选择 k 范围 [0, n^2] 作为示例
    if n <= 0:
        return  # 规模非法，不输出

    k = random.randint(0, n * n)

    if n == 1:
        print(0)
    else:
        r = int(math.sqrt(9 + 8 * (k + n)))
        y = (-3 + r) // 2
        print(n - y)

if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(10)