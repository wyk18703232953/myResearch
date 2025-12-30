def main(n):
    """
    将原始逻辑封装到 main(n) 中，并根据 n 生成测试数据。
    这里约定测试数据为：
      - t = n
      - 对于第 i 个测试用例：
            n_i = i + 1
            k_i = i * i      （可按需修改生成规则）
    """
    t = n

    for i in range(t):
        n_i = i + 1
        k_i = i * i

        n_val = n_i
        k_val = k_i

        if n_val >= 32:
            print("YES", n_val - 1)
            continue

        possibleSize = -1
        sz = 1

        while sz <= n_val:
            req_cuts = 2 ** (sz + 1) - 2 - sz
            tot_cuts = ((4 ** sz) - 1) // 3 + (((2 ** sz) - 1) ** 2) * (((4 ** (n_val - sz)) - 1) // 3)

            if req_cuts > k_val:
                break
            if tot_cuts >= k_val:
                possibleSize = sz
                break

            sz += 1

        if possibleSize != -1:
            print("YES", n_val - possibleSize)
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5) 作为规模为 5 的测试
    main(5)