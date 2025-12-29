import math
import random

MOD = 1000000007

def main(n):
    # 生成测试数据：在 [0, n] 范围内随机生成一个整数作为测试用的 n
    test_n = random.randint(0, n)

    ans = [1, 3, 15, 133, 2025, 37851, 1030367, 36362925]

    # 原本程序的逻辑是对输入 n 进行计算，这里用 test_n 代替
    if test_n % 2 == 1 and test_n // 2 < len(ans):
        result = ans[test_n // 2] * math.factorial(test_n) % MOD
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(7)，规模为 7，可按需要修改
    main(7)