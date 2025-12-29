import random

def main(n):
    # 生成测试数据：m 在 [n, 2n] 之间，保证每个位置大概率被多次选中
    m = random.randint(n, 2 * n)

    square = [0] * n
    # 生成 m 个 1..n 之间的随机位置
    l = [random.randint(1, n) for _ in range(m)]

    for x in l:
        square[x - 1] += 1

    print(min(square))