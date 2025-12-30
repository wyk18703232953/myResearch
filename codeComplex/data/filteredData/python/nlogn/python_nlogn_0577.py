def sfy(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    elif n == 3:
        return [1, 1, 3]
    else:
        if n % 2 == 0:
            return [1] * (n // 2) + [2 * x for x in sfy(n // 2)]
        else:
            return [1] * (1 + n // 2) + [2 * x for x in sfy(n // 2)]


def main(n):
    # 这里根据 n 生成测试数据：本题逻辑中 n 本身就是规模参数
    # 如需复杂测试数据，可在此扩展生成逻辑
    res = sfy(n)
    print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    # 示例：可在此指定规模 n 进行测试
    main(10)