def solve_one(n, k):
    if n > 31:
        # print("YES", n - 1)
        pass
        return

    if k > (4 ** n - 1) // 3:
        # print("NO")
        pass
        return

    l = (4 ** n - 1) // 3
    i = 1
    j = 0
    k1 = k

    while i <= n:
        k -= (2 ** i - 1)
        j = i
        if k < 0:
            j = j - 1
            k += (2 ** i - 1)
            break
        i += 1

    k2 = k1 - k
    k3 = (2 ** (j + 1) - 1) * ((4 ** (n - j) - 1) // 3)

    if l - k2 - k3 >= k:
        # print("YES", n - i + 1)
        pass

    else:
        # print("NO")
        pass


def main(n):
    """
    规模参数 n 用于生成测试数据并调用 solve_one。
    这里按如下方式生成测试数据：
      - 测试次数 t = n
      - 第 i 个测试用例：n_i = i（从 1 到 n）
      - 对于每个 n_i，k_i 取中间值：k_i = ((4**n_i - 1)//3) // 2
    可根据需要修改生成策略。
    """
    t = n
    for i in range(1, t + 1):
        ni = i
        li = (4 ** ni - 1) // 3
        ki = max(1, li // 2)  # 确保 k >= 1
        solve_one(ni, ki)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 组测试数据并输出结果
    main(5)