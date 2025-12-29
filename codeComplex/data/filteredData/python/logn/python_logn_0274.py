mod = 10**9 + 7

def main(n: int):
    """
    规模 n：用来生成测试数据的第二个参数
    测试数据生成规则（示例）：
      - x 在 [-n, n] 范围内取一个确定的值，这里取 x = n - 1
    """
    # 生成测试数据
    x = n - 1  # 可按需要调整生成规则

    if x > 0:
        ans = pow(2, n + 1, mod) * x - pow(2, n, mod) + 1
    else:
        ans = 0
    ans %= mod
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)