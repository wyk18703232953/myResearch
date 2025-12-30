import random


def max_xor_naive(l, r):
    max_xor = 0
    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            xor_val = a ^ b
            if xor_val > max_xor:
                max_xor = xor_val
    return max_xor


def max_xor_efficient(l, r):
    s1 = bin(l)[2:]
    s2 = bin(r)[2:]
    l1 = len(s1)
    l2 = len(s2)
    if l1 < l2:
        return (1 << l2) - 1
    for i in range(l1):
        if s1[i] != s2[i]:
            return (1 << (l1 - i)) - 1
    return 0


def main(n):
    # 生成测试数据：
    # n 作为上界规模，在 [1, n] 内随机生成 l, r 且 l <= r
    if n < 1:
        return
    l = random.randint(1, n)
    r = random.randint(l, n)

    ans2 = max_xor_efficient(l, r)
    print(ans2)


if __name__ == "__main__":
    # 示例规模，可根据需要修改
    main(1000)