def main(n: int):
    # 生成测试数据：根据 n 构造一个合法的 k
    # 原逻辑中二分求解的是 ANS，使得：
    # (n-ANS)*(n-ANS+1)//2 - ANS == k
    # 我们现在反向：先选择一个 ANS，然后计算对应的 k，再用原逻辑求回 ANS。
    # 为了全面测试，这里选取一个中间值作为 ANS_test
    ANS_test = n // 3  # 可按需修改为任意 0 <= ANS_test <= n

    # 依照原公式生成 k
    k = (n - ANS_test) * (n - ANS_test + 1) // 2 - ANS_test

    # 以下是原逻辑的二分部分
    MIN = 0
    MAX = n

    while True:
        ANS = (MIN + MAX) // 2
        val = (n - ANS) * (n - ANS + 1) // 2 - ANS

        if val > k:
            MIN = ANS + 1
        elif val < k:
            MAX = ANS - 1

        else:
            # print(ANS)
            pass
            break


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改或由外部调用传入
    main(10)