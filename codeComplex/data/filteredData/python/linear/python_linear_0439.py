import math
import random

def getx(n):
    return math.floor(math.sqrt(n))

def getans(n, x, data):
    l1 = data[:]  # 使用生成的测试数据
    l2 = []
    i = 0
    while i < n:
        l2 = l2 + sorted(l1[i:i + x])
        i += x
    return l2

def main(n):
    # 生成规模为 n 的测试数据，这里用 1..n 的排列作为示例
    data = list(range(1, n + 1))
    random.shuffle(data)

    a = getx(n)
    ans = getans(n, a, data)
    ans1 = [str(i) for i in ans]
    print(' '.join(ans1))

# 示例：调用 main(10)
# main(10)