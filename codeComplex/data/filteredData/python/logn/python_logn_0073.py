def main(n):
    # 映射：n -> l, r，使得规模随 n 增大
    # 这里构造一个区间 [l, r]，长度与 n 相关且确定性
    l = n
    r = 2 * n

    limit = l ^ r

    if limit != 0:
        limit = len(bin(limit)) - 2
        maxXor = '1' * limit
        result = int(maxXor, 2)

    else:
        result = 0

    # print(result)
    pass
if __name__ == "__main__":
    main(10)