def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里约定：x = n, k = n
    x = n
    k = n

    if x == 0:
        # print(0)
        pass
        return

    mod = 10**9 + 7
    ans = 1 + (2 * x - 1) * pow(2, k, mod)
    # print(ans % mod)
    pass
if __name__ == "__main__":
    # 示例：当需要测试时，可修改这里的 n
    main(10)