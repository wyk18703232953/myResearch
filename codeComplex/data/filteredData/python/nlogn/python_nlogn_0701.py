from collections import Counter
import random

def main(n: int):
    # 生成测试数据：n 个非负整数
    # 这里使用随机生成，也可按需修改生成策略
    random.seed(0)
    A = [random.randint(0, 10**6) for _ in range(n)]

    A.sort()
    C = Counter(A)
    dou = 0

    for c in C:
        dou += C[c] - 1

        if C[c] >= 2 and C.get(c - 1, 0) != 0:
            print("cslnb")
            return

    if dou >= 2:
        print("cslnb")
        return

    ANS = 0
    for i in range(n):
        if A[i] < i:
            print("cslnb")
            return
        ANS += (A[i] - i) % 2

    if ANS % 2 == 0:
        print("cslnb")
    else:
        print("sjfnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)