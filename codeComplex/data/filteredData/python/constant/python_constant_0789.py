import math
import random

def main(n):
    # 生成 n 个测试数据，每个为 1 到 10^9 之间的整数
    test_cases = [random.randint(1, 10**9) for _ in range(n)]

    for num in test_cases:
        s = 1
        ch = 0
        for _ in range(1, 31):
            s *= 2
            if num % s != 0:
                continue
            d = math.isqrt(num // s)
            if d * d == num // s:
                ch = 1
                break
        if ch:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)