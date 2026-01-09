def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main(n):
    # 根据规模 n 生成区间 [l, r]
    # 这里设定：搜索区间长度为 n，从 1 开始
    l, r = 1, n

    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            for c in range(b + 1, r + 1):
                if gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) != 1:
                    # print(a, b, c)
                    pass
                    return
    # print(-1)
    pass
if __name__ == "__main__":
    # 示例：可修改 n 来控制搜索区间大小
    main(10)