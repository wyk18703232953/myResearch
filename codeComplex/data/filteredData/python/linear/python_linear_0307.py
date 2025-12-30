import math
import random

def main(n):
    # 生成测试数据：a 为长度为 n 的整数数组
    # 这里示例为在 [0, 10^9] 区间内均匀随机生成
    a = [random.randint(0, 10**9) for _ in range(n)]

    x = 10**9 + 2
    y = 0
    for i in range(n):
        val = math.ceil((a[i] - i) / n) * n + i + 1
        if x > val:
            x = val
            y = i + 1

    print(y)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)