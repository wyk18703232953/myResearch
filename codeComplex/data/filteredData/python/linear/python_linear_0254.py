def main(n: int):
    # 根据规模 n 生成测试数据（这里简单设定 k，与 n 同奇偶且不超过 2n-2）
    # 可按需要自行修改生成逻辑
    k = max(1, min(2 * n - 2, n | 1))  # 生成一个不大于 2n-2 的奇数 k，且至少为 1

    # print("YES")
    pass
    # 第一行
    # print("." * n)
    pass

    if k & 1:
        if k <= n - 2:
            tmp = (n - k) >> 1
            # 第二行
            # print("." * tmp + "#" * k + "." * tmp)
            pass
            # 第三行
            # print("." * n)
            pass

        else:
            # 第二行
            # print("." + "#" * (n - 2) + ".")
            pass
            k -= n - 2
            # 第三行
            left = k >> 1
            mid = n - k - 2
            # print("." + "#" * left + "." * mid + "#" * left + ".")
            pass

    else:
        k >>= 1
        for _ in range(2):
            # print("." + "#" * k + "." * (n - k - 1))
            pass

    # 最后一行
    # print("." * n)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(7)