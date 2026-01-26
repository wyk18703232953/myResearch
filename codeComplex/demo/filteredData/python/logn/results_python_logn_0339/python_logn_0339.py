def main(n):
    # 生成测试数据：x, k 与规模 n 相关
    # 这里只是一个示例策略，可以根据需要调整生成规则
    x = n
    k = n  # 或者例如：k = n // 2 等其他方式

    mod = 10**9 + 7
    e = (x * pow(2, k, mod)) % mod
    s = (e - pow(2, k, mod)) % mod
    f = lambda x: (x * (x + 1)) % mod
    ans = ((f(e) - f(s)) * pow(2, k * (mod - 2), mod)) % mod
    result = ans if x != 0 else 0

    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例调用，可以根据需要修改测试规模
    main(10)