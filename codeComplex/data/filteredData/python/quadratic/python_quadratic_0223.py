def main(n):
    # 根据 n 生成测试数据
    # 这里简单生成：s 为严格递增序列，c 为递增费用
    # 你可以按需要自行修改生成方式
    s = list(range(1, n + 1))
    c = list(range(1, n + 1))

    INF = 10 ** 12
    d = {}

    # 预处理：对每个 i，找到一个 j>i 且 s[i] < s[j] 的最小 c[i] + c[j]
    for i in range(n - 1):
        ans = INF
        for j in range(i + 1, n):
            if s[i] < s[j]:
                ans = min(ans, c[i] + c[j])
        d[i] = ans

    # 计算答案：找到 i<j<k 且 s[i] < s[j] < s[k] 的最小 c[i] + c[j] + c[k]
    ans = INF
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if s[i] < s[j]:
                ans = min(ans, c[i] + d[j])

    if ans == INF:
        # print(-1)
        pass

    else:
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)