import random
import sys


def main(n):
    # 生成测试数据 A，长度为 n，元素为 1..3 之间的整数
    A = [random.randint(1, 3) for _ in range(n)]

    # 为了可重复测试，也可以手动指定一个例子：
    # A = [2, 1, 1, 1, 3, 1, 2, 3, 1, 3]
    # n = len(A)

    if sum(A) < 2 * n - 2:
        print("NO")
        return

    ONES = A.count(1)
    print("YES", min(n - 1, n - ONES + 1))

    NOONE = []
    for i in range(n):
        if A[i] != 1:
            NOONE.append([A[i], i + 1])

    ANS = []
    for i in range(1, len(NOONE)):
        ANS.append((NOONE[i - 1][1], NOONE[i][1]))
        NOONE[i - 1][0] -= 1
        NOONE[i][0] -= 1

    NOONE = [[1, NOONE[-1][1]]] + NOONE[0:-1] + [[NOONE[-1][0] - 1, NOONE[-1][1]]]

    LENNO = len(NOONE)
    j = 0
    for i in range(n):
        while j < LENNO and NOONE[j][0] == 0:
            j += 1
        if A[i] != 1:
            continue
        ANS.append((i + 1, NOONE[j][1]))
        NOONE[j][0] -= 1

    print(len(ANS))
    for a, b in ANS:
        print(a, b)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)