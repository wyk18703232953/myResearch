def main(n):
    # 解释输入规模映射：
    # n -> 列表 a 的长度
    # m 在原代码中未被实际使用，这里设为与 n 相关的确定性值
    m = n * 2 + 1

    # 构造确定性输入数据：
    # a 为长度为 n 的整数列表
    # 使用简单算术规则生成，保持可规模化与确定性
    a = [(i * 3) % (n + 5) + (i // 2) for i in range(n)]

    a.sort()
    mx = a[-1] if a else 0
    t = 0
    ans = 0
    for i in a:
        if i > 0:
            if i > t:
                t += 1
            ans += i - 1
    ans -= mx - t
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)