mod = 1000000007

def main(n: int):
    """
    使用规模 n 生成测试数据 (x, k)，并计算原程序中的答案。
    可以根据需要修改测试数据生成规则。
    """
    # 示例：根据 n 生成一组确定性的测试数据
    # 避免 x=0 的特例只测试到一种情况，这里简单设置：
    x = n % mod               # 确保 0 <= x < mod
    k = n                     # 令 k = n，可以按需调整规则

    if x == 0:
        ans = 0

    else:
        ans = (pow(2, k + 1, mod) * x % mod
               - (pow(2, k, mod) - 1 + mod) % mod
               + mod) % mod

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)