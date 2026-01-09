def max_xor_naive(l, r):
    max_xor = 0
    xor = 0
    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            xor = a ^ b
            if xor > max_xor:
                max_xor = xor
    return max_xor

def max_xor_efficient(l, r):
    s1 = bin(l)[2:]
    s2 = bin(r)[2:]
    l1 = len(s1)
    l2 = len(s2)
    if l1 < l2:
        return pow(2, l2) - 1
    for i in range(0, l1):
        if s1[i] != s2[i]:
            return pow(2, l1 - i) - 1
    return 0

def main(n):
    # 解释：将 n 映射为一组区间 [l, r]
    # 我们生成 n 组测试，每组的 r 规模为 O(n)
    # 第 i 组：l = i, r = 2*i + (n // 2)
    # 保证 l <= r 且可随 n 线性扩展
    results = []
    for i in range(1, n + 1):
        l = i
        r = 2 * i + (n // 2)
        if l > r:
            l, r = r, l
        ans2 = max_xor_efficient(l, r)
        results.append(ans2)
    # 输出最后一个结果，以避免输出过大
    if results:
        # print(results[-1])
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)