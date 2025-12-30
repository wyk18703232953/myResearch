def cntbit(n: int) -> int:
    ans = 0
    while n:
        ans += 1
        n //= 2
    return ans


def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设定：
    # l 为 n，r 为 2n+1，保证 l <= r 且有一定差异
    l = n
    r = 2 * n + 1

    c1 = cntbit(l)
    c2 = cntbit(r)

    if c2 > c1:
        print(2 ** c2 - 1)
    else:
        x = l ^ r
        c = cntbit(x)
        print(2 ** c - 1)


if __name__ == "__main__":
    # 示例调用，实际使用时可在外部调用 main(k)
    main(10)