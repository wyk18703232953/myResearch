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

def good(A, X, Y):
    n = len(A)
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

def generate_points(n):
    # 生成规模为 n 的测试点集，坐标范围可按需调整
    A = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        A.append([x, y])
    return A

def main(n):
    if n <= 4:
        print("YES")
        return

    A = generate_points(n)

    X, Y, Z = A[0], A[1], A[2]

    if good(A, X, Y) or good(A, Y, Z) or good(A, X, Z):
        print("YES")
    else:
        print("NO")

# 示例调用
# main(10)