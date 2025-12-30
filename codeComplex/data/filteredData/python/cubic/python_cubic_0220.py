import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 设 rn, gn, bn 均与 n 成正比，这里简单设为 n
    rn = n
    gn = n
    bn = n

    # 随机生成颜色数组，元素为 1~10^3 之间的整数
    rr = [random.randint(1, 1000) for _ in range(rn)]
    gg = [random.randint(1, 1000) for _ in range(gn)]
    bb = [random.randint(1, 1000) for _ in range(bn)]

    rr.sort(reverse=True)
    gg.sort(reverse=True)
    bb.sort(reverse=True)

    # 三维 DP
    dp = [[[-1] * (bn + 1) for _ in range(gn + 1)] for _ in range(rn + 1)]
    dp[0][0][0] = 0
    ans = 0

    for i in range(rn + 1):
        for j in range(gn + 1):
            for k in range(bn + 1):
                pre = dp[i][j][k]
                if pre == -1:
                    continue
                if pre > ans:
                    ans = pre
                if i < rn and j < gn:
                    val = pre + rr[i] * gg[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < rn and k < bn:
                    val = pre + rr[i] * bb[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < gn and k < bn:
                    val = pre + gg[j] * bb[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模 n=3
    main(3)