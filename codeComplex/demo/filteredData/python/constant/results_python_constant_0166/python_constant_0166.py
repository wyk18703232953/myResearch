def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main(n: int):
    """
    n 为规模参数。
    这里根据 n 生成区间 [l, r]，例如固定长度为 n，从 1 到 n。
    如需其他生成方式（如 [n, 2n]），可自行调整。
    """
    l, r = 1, n
    f = 0

    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            for c in range(b + 1, r + 1):
                if (gcd(a, b) == 1) and (gcd(b, c) == 1) and (gcd(a, c) != 1):
                    # print(a, b, c)
                    pass
                    f = 1
                    break
            if f == 1:
                break
        if f == 1:
            break

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # 示例：规模 n = 20
    main(20)