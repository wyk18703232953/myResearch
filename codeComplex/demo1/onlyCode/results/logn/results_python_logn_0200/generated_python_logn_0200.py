import math
import random

def main(n):
    # 生成测试数据：随机生成 s，范围设为 [1, n]
    if n <= 0:
        print(0)
        return

    s = random.randint(1, n)

    c = 0
    i = n
    # 按原逻辑枚举 [s, min(s+1000, n)]
    for i in range(s, min(s + 1000, n + 1)):
        if i - sum(map(int, str(i))) >= s:
            c += 1
    # 后续区间用公式累加
    c += max(0, n - i)
    print(c)


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10**6)