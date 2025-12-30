import random

def main(n):
    # 生成规模为 n 的测试数据：三点 (x, y)，坐标范围可按需调整
    # 这里将 x, y 控制在 [0, n] 范围内
    a = [random.randint(0, n), random.randint(0, n)]
    b = [random.randint(0, n), random.randint(0, n)]
    c = [random.randint(0, n), random.randint(0, n)]

    # 按原程序逻辑排序
    a, b, c = sorted([a, b, c])

    path = []
    for i in range(min(a[1], b[1], c[1]), max(a[1], b[1], c[1]) + 1):
        path.append((b[0], i))
    for i in range(a[0], b[0] + 1):
        path.append((i, a[1]))
    for i in range(b[0], c[0] + 1):
        path.append((i, c[1]))

    unique_path = list(set(path))
    print(len(unique_path))
    for x, y in unique_path:
        print(x, y)


if __name__ == "__main__":
    # 可在此修改 n 的默认测试规模
    main(10)