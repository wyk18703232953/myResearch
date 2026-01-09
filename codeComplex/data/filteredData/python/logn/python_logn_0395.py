def main(n):
    # 在原程序中，n 是输入的第一个整数，k 是第二个整数
    # 这里将实验规模参数 n 直接映射为原程序中的 n
    original_n = max(1, n)  # 保证 n 至少为 1，避免无意义的 0 情况
    # 为了使规模随 n 增长，这里令 k 为 n 的平方
    k = original_n * original_n

    def area(height):
        return original_n * height

    def bin_search(low, high):
        if high == low:
            return high
        if high - low == 1:
            if area(low) >= k:
                return low
            return high
        midd = (high + low) // 2
        if area(midd) > k:
            return bin_search(low, midd)
        return bin_search(midd, high)

    result = bin_search(0, 10**18)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)