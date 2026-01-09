mod = 10 ** 9 + 7

def main(n: int):
    """
    n 为规模，用来生成测试数据：
    这里约定：
      x = n
      k = n
    可根据需要自行调整生成规则。
    """
    x = n
    k = n

    if x != 0:
        ans = (pow(2, k + 1, mod) * x - pow(2, k, mod) + 1) % mod

    else:
        ans = 0

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)