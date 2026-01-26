DV = 10**9 + 7

def solve(x, k):
    mult = pow(2, k, DV)
    if x == 0:
        return 0

    else:
        return (2 * mult * x - mult + 1) % DV

def generate_test_data(n):
    # 根据规模 n 生成一组 (x, k) 测试数据
    # 这里简单设定：
    #   x = n
    #   k = n 的二进制位数
    if n <= 0:
        x = 0
        k = 0

    else:
        x = n
        k = n.bit_length()
    return x, k

def main(n):
    x, k = generate_test_data(n)
    ans = solve(x, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可修改为任意想测试的规模
    main(10)