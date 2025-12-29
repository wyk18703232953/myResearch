from sys import stdout
import random

def count(audrey, imba, banget):
    return (imba - audrey - 1) % (banget - 1)

def main(n):
    # 1. 根据 n 生成测试数据
    # 生成长度为 n 的数组 L，元素为 1~10^9 的随机整数
    L = [random.randint(1, 10**9) for _ in range(n)]
    # 生成随机查询次数 q (1 到 2n)
    q = random.randint(1, 2 * n)
    # 生成 q 个随机查询 m (1 到 2n)
    queries = [random.randint(1, 2 * n) for _ in range(q)]

    # 2. 原逻辑开始
    maxi = max(L)
    indexmax = L.index(maxi)
    P = []

    # 预处理前 indexmax 次对决
    for _ in range(indexmax):
        P.append((L[0], L[1]))
        if L[0] < L[1]:
            L.append(L.pop(0))
        else:
            L.append(L.pop(1))

    Y = tuple(L[1:])  # 循环部分

    # 3. 按照 queries 依次输出结果（替代原 input()/stdin）
    for m in queries:
        if m <= indexmax:
            a, b = P[m - 1]
            stdout.write(f"{a} {b}\n")
        else:
            stdout.write(f"{maxi} {Y[count(indexmax, m, n)]}\n")


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)