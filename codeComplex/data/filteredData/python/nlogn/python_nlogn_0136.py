def main(n):
    # 对应原程序中的 n：数组长度
    # 构造确定性的 m, k
    m = n * 2
    k = n

    # 构造确定性的数组 a，长度为 n
    # 示例：a[i] = (i * 3) % (n + 5) + 1，确保为正整数
    a = [(i * 3) % (n + 5) + 1 for i in range(n)]

    # 原始逻辑开始
    a = sorted(a)
    res_candidates = [x for x in range(n + 1) if sum(a[n - x:]) + k >= m + x]
    ans = min(res_candidates) if res_candidates else -1
    print(ans)
    return ans


if __name__ == "__main__":
    main(10)