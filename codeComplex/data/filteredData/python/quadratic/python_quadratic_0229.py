import math
import sys
import random

def main(n):
    # 生成测试数据
    # 随机生成一个长度为 n 的数组 s，元素为 1~10^6
    # 随机生成对应的代价数组 ce，元素为 1~10^6
    random.seed(0)
    s = [random.randint(1, 10**6) for _ in range(n)]
    ce = [random.randint(1, 10**6) for _ in range(n)]

    best = 10**9
    for j in range(1, n - 1):
        a = ce[j]
        b = 10**9
        c = 10**9
        for i in range(j - 1, -1, -1):
            if s[i] < s[j]:
                b = min(b, ce[i])
        for k in range(j + 1, n):
            if s[k] > s[j]:
                c = min(c, ce[k])
        best = min(best, a + b + c)

    if best >= 10**9:
        print(-1)
    else:
        print(best)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)