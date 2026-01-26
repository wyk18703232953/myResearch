def main(n):
    # 映射含义：
    # n: 数组长度
    # a, b 由 n 确定性构造，且满足 1 <= b <= n, 1 <= a <= n-b+1
    if n < 2:
        # print(0)
        pass
        return

    # 构造参数 a, b
    b = max(1, n // 3)
    a = max(1, min(n - b + 1, n // 2))

    # 构造数组 c，长度为 n，确定性递增构造，保证有序后仍有有趣结构
    c = [(i * 2 + (i // 3)) for i in range(n)]

    # 原始逻辑开始
    c.sort()
    l = c[b - 1]
    r = 0
    ok = False
    for i in range(b, n - a + 1):
        if c[i] > l:
            ok = True
            r = c[i]
            break
    if ok:
        # print(r - l)
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模实验
    main(10)