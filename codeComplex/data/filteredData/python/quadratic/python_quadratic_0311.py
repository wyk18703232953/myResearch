from collections import Counter
import math
import random

def makedict(var):
    return dict(Counter(var))

def main(n):
    # 生成测试数据：
    # n 为数组长度
    # 随机生成 k（1 <= k <= n）
    # 随机生成数组 num，元素范围可自行调整
    if n <= 0:
        return 0.0

    k = random.randint(1, n)
    # 示例：生成 [-100, 100] 区间内的随机整数
    num = [random.randint(-100, 100) for _ in range(n)]

    maxi = 0.0
    for i in range(n):
        count = 1
        sumt = num[i]
        for j in range(i + 1, n):
            sumt += num[j]
            count += 1
            if count >= k:
                maxi = max(maxi, sumt / count)

    if k == 1:
        result = max(maxi, max(num))
    else:
        result = maxi

    # 为方便查看结果，这里打印；也可以只返回 result
    print("n =", n)
    print("k =", k)
    print("num =", num)
    print("answer =", result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(10) 生成规模为 10 的随机测试数据并求解
    main(10)