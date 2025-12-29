import random

def main(n):
    # 生成测试数据
    # 约定：m 与 n 同规模，这里设 m = n
    m = n

    # 生成 b 和 g，保证非空且有一定随机性
    # 数值范围可以根据需要调整
    b = [random.randint(1, 100) for _ in range(n)]
    g = [random.randint(1, 100) for _ in range(m)]

    # 以下为原逻辑
    Sum = 0
    for j in range(n):
        Sum += b[j] * m
    b.sort()
    for i in range(m):
        Sum += max(0, g[i] - b[-1])
    if min(g) < max(b):
        print(-1)
    elif min(g) == max(b):
        print(Sum)
    else:
        Sum += b[-1] - b[-2]
        print(Sum)


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)