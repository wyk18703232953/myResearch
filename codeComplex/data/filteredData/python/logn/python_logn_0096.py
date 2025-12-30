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
    # 根据规模 n 生成测试数据：
    # 令 l ∈ [0, n]，r ∈ [l, 2n]，保证有一定区间长度
    if n < 1:
        n = 1
    l = random.randint(0, n)
    r = random.randint(l, 2 * n)

    # 使用高效算法计算并输出结果
    ans2 = max_xor_efficient(l, r)
    print(ans2)

if __name__ == "__main__":
    # 示例：使用 n=100 作为规模
    main(100)