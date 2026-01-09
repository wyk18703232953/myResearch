MOD = 10**9 + 7

def power(a, b, z):
    if b == 0:
        return 1
    temp = power(a, b // 2, z)
    if b % 2 == 0:
        return (temp * temp) % z
    return (a * temp * temp) % z

def main(n):
    """
    n 为规模参数，用来生成测试数据 (x, k)。
    这里简单地通过 n 构造一个确定性的测试数据：
      x = n
      k = n
    可以根据需要修改为更复杂的生成方式。
    """
    x = n
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        z = MOD
        res_n = (power(2, k + 1, z) * x) % z
        res_m = power(2, k, z)
        # print((res_n - res_m + 1) % z)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n 的取值
    main(10)