def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设 x, k 与 n 有关，可按需求自定义生成策略。
    # 示例：x = n，k = n 的平方（只要保证非负整数即可）
    x = n
    k = n * n

    if x == 0:
        print(0)
        return

    mod = 10 ** 9 + 7

    res = x * pow(2, k + 1, mod) % mod
    res = ((res - (pow(2, k, mod) - 1)) % mod + mod) % mod

    print(res)


if __name__ == "__main__":
    # 示例调用
    main(10)