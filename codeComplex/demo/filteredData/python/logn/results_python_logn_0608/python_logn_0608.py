def main(n):
    import math

    # 确定性生成 k，与 n 同级别规模
    k = n * (n + 1) // 2

    if n == 1:
        # print(0)
        pass

    else:
        r = int(math.isqrt(9 + 8 * (k + n)))
        y = (-3 + r) // 2
        # print(n - y)
        pass
if __name__ == "__main__":
    main(10)