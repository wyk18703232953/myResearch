from math import ceil
import random

def main(n):
    # 生成测试数据：a 为长度为 n 的整数数组
    # 这里示例用 1 到 10^9 之间的随机数
    a = [random.randint(1, 10**9) for _ in range(n)]

    ans = 10**6
    value = 10**9 + 7

    for i in range(n):
        t = ceil((a[i] - i) / n)
        tmp = i + n * t
        if tmp < value:
            value = tmp
            ans = i + 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)