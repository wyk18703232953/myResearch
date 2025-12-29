import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 原代码有三个数组 x, y, z，长度分别为 a, b, c
    # 这里统一令 a = b = c = n
    a = b = c = n

    # 生成随机数据（可按需要调整范围）
    x = [random.randint(1, 10**9) for _ in range(a)]
    y = [random.randint(1, 10**9) for _ in range(b)]
    z = [random.randint(1, 10**9) for _ in range(c)]

    x.sort(reverse=True)
    y.sort(reverse=True)
    z.sort(reverse=True)

    a += 1
    b += 1
    c += 1

    x = [0] + x
    y = [0] + y
    z = [0] + z

    # 正确初始化三维 DP 数组
    best = [[[0] * c for _ in range(b)] for _ in range(a)]

    ans = 0
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if (i + j + k) % 2 == 0:
                    aa = bb = cc = 0
                    if i > 0 and j > 0:
                        aa = best[i - 1][j - 1][k] + x[i] * y[j]
                    if i > 0 and k > 0:
                        bb = best[i - 1][j][k - 1] + x[i] * z[k]
                    if j > 0 and k > 0:
                        cc = best[i][j - 1][k - 1] + y[j] * z[k]
                    best[i][j][k] = max(aa, bb, cc)
                    if best[i][j][k] > ans:
                        ans = best[i][j][k]

    print(ans)


if __name__ == "__main__":
    # 示例：n = 3
    main(3)