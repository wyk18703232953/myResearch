import random

def main(n):
    # 根据 n 生成测试数据
    # 约定：m 在 [1, n] 范围内，a 为长度为 m 的 1..n 之间的随机整数
    m = random.randint(1, n)
    a = [random.randint(1, n) for _ in range(m)]

    count = [0] * n
    for i in range(m):
        count[a[i] - 1] += 1
    print(min(count))