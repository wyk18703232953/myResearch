import random

def main(n):
    # 1. 生成规模为 n 的测试数据：三点 (x, y)
    # 为了简单，令坐标在 [0, n] 范围内
    a = [random.randint(0, n), random.randint(0, n)]
    b = [random.randint(0, n), random.randint(0, n)]
    c = [random.randint(0, n), random.randint(0, n)]

    # 保持与原程序行为一致：按字典序排序三个点
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
    for p in unique_path:
        print(*p)


if __name__ == "__main__":
    # 示例：将 n 设为 10，可根据需要修改
    main(10)