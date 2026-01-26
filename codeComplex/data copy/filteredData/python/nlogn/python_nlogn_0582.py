def main(n):
    ans = []
    p = 1
    fin = n

    # 原逻辑：根据 n 生成 ans 列表
    while len(ans) < n - 1:
        for _ in range(fin - (n // (2 ** p))):
            ans.append(2 ** (p - 1))
            fin -= 1
        p += 1

    if 2 ** (p - 2) + 2 ** (p - 1) <= n:
        ans.append(2 ** (p - 1) + 2 ** (p - 2))

    else:
        ans.append(2 ** (p - 1))

    s = " ".join(str(x) for x in ans)
    # print(s)
    pass


# 示例：根据需要调用 main(n)
if __name__ == "__main__":
    # 这里可以根据需要修改 n 的测试规模
    test_n = 10
    main(test_n)