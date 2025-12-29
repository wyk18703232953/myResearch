def main(n: int):
    # 这里根据 n 生成测试数据，本题原逻辑与 n 直接相关，无需额外结构。
    ans = []
    m = 1
    while n > 3:
        ans += [m] * (n - n // 2)
        n //= 2
        m *= 2
    if n == 3:
        ans += [m, m, m * 3]
    elif n == 2:
        ans += [m, m * 2]
    else:
        ans += [m]
    print(*ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 测试不同规模
    main(10)