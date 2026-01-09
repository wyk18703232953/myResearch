def main(n):
    # 解释输入规模：n 控制 [l, r] 区间大小
    # 这里构造确定性的 l, r：
    # 令 l = n，r = 2n（且 r >= l）
    l = n
    r = 2 * n

    p = l
    lp = -1
    while p:
        p = p >> 1
        lp += 1

    q = r
    rp = -1
    while q:
        q = q >> 1
        rp += 1

    s = max(lp, rp)

    ans = 0

    while s >= 0:
        if (l >> s) & 1 != (r >> s) & 1:
            ans |= ((r >> s) & 1) << s
            break
        s -= 1

    s -= 1

    while s >= 0:
        ans |= 1 << s
        s -= 1

    return ans


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    result = main(10)
    # print(result)
    pass