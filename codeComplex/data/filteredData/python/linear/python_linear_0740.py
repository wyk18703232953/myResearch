from sys import stdout
import random

def count(audrey, imba, banget):
    return (imba - audrey - 1) % (banget - 1)

def main(n):
    # 1. 生成测试数据
    # n: 数组规模
    # 生成 n 个互不相同的正整数
    L = random.sample(range(1, 10 * n + 1), n)

    # 为了体现查询效果，生成 q 与 n 同级
    q = n
    # 生成 q 个查询：随机在 [1, 2n] 范围内
    queries = [random.randint(1, 2 * n) for _ in range(q)]

    # 2. 原逻辑开始
    maxi = max(L)
    indexmax = L.index(maxi)
    P = []
    # 预处理阶段：记录最大值出现前的“对战”
    for _ in range(indexmax):
        P.append((L[0], L[1]))
        if L[0] < L[1]:
            L.append(L.pop(0))
        else:
            L.append(L.pop(1))
    Y = tuple(L[1:])

    # 3. 处理查询
    out_lines = []
    for m in queries:
        if m <= indexmax:
            a, b = P[m - 1]
            out_lines.append(f"{a} {b}")
        else:
            idx = count(indexmax, m, n)
            out_lines.append(f"{maxi} {Y[idx]}")
    stdout.write("\n".join(out_lines) + "\n")


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)