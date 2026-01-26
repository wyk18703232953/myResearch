def main(n):
    # 映射：n -> (x, k)
    # 设 x = n，k = n，用于规模控制
    MOD = 1000000007
    x = n
    k = n

    if x == 0:
        result = 0

    else:
        u = (pow(2, k, MOD) * (2 * x - 1) + 1) % MOD
        result = int(u)
    return result

if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 的大小
    # print(main(10))
    pass