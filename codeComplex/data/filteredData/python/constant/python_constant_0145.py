def prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    limit = int(x ** 0.5) + 1
    for j in range(3, limit, 2):
        if x % j == 0:
            return False
    return True


def main(n):
    """
    n 为规模，同时作为原程序中的目标数。
    可以在此根据 n 生成测试数据，如果需要更复杂的测试数据，
    可在这里扩展。目前直接用 n 作为原程序中的输入。
    """
    for j in range(2, int(n / 2) + 1):
        if not prime(j) and not prime(n - j):
            # print(j, n - j)
            pass
            break


if __name__ == "__main__":
    # 示例：调用 main(100) 进行测试
    main(100)