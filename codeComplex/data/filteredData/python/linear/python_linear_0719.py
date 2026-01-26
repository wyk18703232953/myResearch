def main(n):
    # 生成确定性输入列表 l，长度为 n
    # 这里使用简单的算术构造：l[i] = (i + 1) * 2
    l = [(i + 1) * 2 for i in range(n)]
    if n == 0:
        return 0
    ans = max(l)
    for i in range(n):
        denom = max(i, n - i - 1)
        if denom == 0:
            # 当 n == 1 且 i == 0 时 denom 为 0，避免除零
            continue
        ans = min(ans, l[i] // denom)
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(10)