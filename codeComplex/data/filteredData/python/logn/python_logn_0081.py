def main(n):
    # 映射 n 为区间 [l, r] 的规模
    # 这里设定 r - l + 1 = n，且从 0 开始
    if n <= 0:
        return 0
    l = 0
    r = n - 1

    q = l ^ r
    a = 1
    while q:
        q //= 2
        a <<= 1
    result = a - 1
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 作为规模参数
    main(10)