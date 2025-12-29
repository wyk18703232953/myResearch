mod = 10**9 + 7

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里简单设置：x = n, k = n
    x = n
    k = n

    if x == 0:
        ans = 0
    else:
        ans = (x * pow(2, k + 1, mod) - (pow(2, k, mod) - 1) + mod) % mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)