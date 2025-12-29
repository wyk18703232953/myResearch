import random

def is_colinear(a1, a2, a3):
    if a1 == a2 or a2 == a3 or a1 == a3:
        return True

    x1, y1 = a1
    x2, y2 = a2
    x3, y3 = a3

    if x1 == x2 or x1 == x3 or x2 == x3:
        return x1 == x2 == x3
    if y1 == y2 or y1 == y3 or y2 == y3:
        return y1 == y2 == y3
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


def main(n):
    # 生成测试数据：n 个点，坐标在 [-10^6, 10^6] 范围内
    # 为了尽量避免完全随机导致的退化情况，保证前 3 个点不完全重合
    A = []

    # 先生成 3 个点
    A.append((random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)))
    A.append((random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)))
    A.append((random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)))

    # 剩余点随机生成
    for _ in range(3, n):
        A.append((random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)))

    if n <= 4:
        print("YES")
        return

    def good(X, Y):
        bad = []
        for i in range(n):
            if not is_colinear(X, Y, A[i]):
                bad.append(A[i])

        if len(bad) <= 2:
            return True

        U, V = bad[0], bad[1]
        for i in range(len(bad)):
            if not is_colinear(U, V, bad[i]):
                return False
        return True

    X, Y, Z = A[0], A[1], A[2]

    if good(X, Y) or good(Y, Z) or good(X, Z):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)