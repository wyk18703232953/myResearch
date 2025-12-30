import math
import random

def main(n: int):
    # 生成测试数据
    # k 在 [1, n] 之间随机选择
    k = random.randint(1, n)
    # 生成长度为 n 的整数数组，元素值在 [-1000, 1000] 之间
    l = [random.randint(-1000, 1000) for _ in range(n)]

    ans = float("-inf")
    for i in range(n):
        c = 0
        sum1 = 0
        for j in range(i, n):
            sum1 += l[j]
            c += 1
            if c >= k:
                ans = max(ans, sum1 / c)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)