import random

def main(n):
    # 生成测试数据：n 行，每行 2 个整数
    # 示例：a 在 [1, 10]，b 在 [1, 10]
    L = []
    for i in range(n):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        L.append([a, b, i + 1])

    # 原逻辑
    L.sort(key=lambda X: (X[0], -X[1], X[2]))
    X = 0
    for i in range(1, n):
        if L[i][1] <= L[i - 1][1]:
            print(L[i][2], L[i - 1][2])
            X = 1
            break
    if X == 0:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)