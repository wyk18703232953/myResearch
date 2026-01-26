MOD = int(1e9 + 7)

def main(n):
    # 将 n 映射为 (x, k)
    # 设定：
    # x = n
    # k = n // 2
    x = n
    k = n // 2

    if x == 0:
        result = 0

    else:
        result = (x * pow(2, k + 1, MOD) - pow(2, k, MOD) + 1) % MOD
    # print(result)
    pass
if __name__ == "__main__":
    main(10)