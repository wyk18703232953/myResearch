def main(n):
    # 生成确定性输入数组，长度为 n
    # 例如：a[i] = i + 1
    a = [i + 1 for i in range(n)]

    ans = float('inf')
    for i in range(n):
        denom = max(i, n - i - 1)
        if denom == 0:
            continue
        ans = min(ans, a[i] // denom)

    if ans == float('inf'):
        ans = 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)