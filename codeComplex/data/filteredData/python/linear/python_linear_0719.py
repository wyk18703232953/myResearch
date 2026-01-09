def main(n):
    # 生成确定性输入数据：长度为 n 的整数列表
    # 这里使用简单的算术构造，使得数据随 n 规模增长
    l = [(i * 3 + 5) for i in range(n)]
    if n == 0:
        # print(0)
        pass
        return
    ans = max(l)
    for i in range(n):
        denom = max(i, n - i - 1)
        if denom == 0:
            continue
        ans = min(ans, l[i] // denom)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)