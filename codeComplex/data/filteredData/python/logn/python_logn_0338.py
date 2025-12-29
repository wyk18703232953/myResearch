M = 10**9 + 7

def main(n):
    """
    n 为规模参数，用来生成测试数据：
    这里简单设定：
      x = n
      k = n // 2
    """
    x = n
    k = n // 2

    if x == 0:
        return 0
    elif k == 0:
        return (x * 2) % M
    else:
        top_sum = (pow(2, k, M) * ((2 * x - 1) % M)) % M + 1
        return top_sum % M


if __name__ == "__main__":
    # 示例：手动指定规模 n 进行测试
    n = 10
    print(main(n))