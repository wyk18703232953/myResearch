from math import *
import random

def main(n):
    # 生成测试数据：k 和 A
    # k 至少为 1，适当限制在 [1, 20] 以避免 2**k 过大
    k = random.randint(1, min(20, max(1, n.bit_length() + 1)))
    # 生成长度为 n 的数组 A，元素为非负整数
    A = [random.randint(0, (1 << k) - 1) for _ in range(n)]

    ans_arr = [0] * n
    lul = 2 ** k - 1

    ans_arr[0] = A[0]
    for j in range(1, n):
        ans_arr[j] = ans_arr[j - 1] ^ A[j]

    d = dict()
    for j in range(n):
        v = ans_arr[j]
        if v in d:
            d[v] += 1
        else:
            d[v] = 1

    def huy(x):
        return x * (x - 1) // 2

    ans = 0
    for j in d:
        now = d[j]
        xor = lul ^ j
        cur = now

        if xor in d:
            now2 = d[xor]
            cur += now2

            ans += huy(cur // 2 + cur % 2)
            ans += huy(cur // 2)
            if j == 0:
                ans += 2 * (cur // 2)
        else:
            if j == 0 or xor == 0:
                ans += 2 * (cur // 2)
            ans += 2 * huy(cur // 2 + cur % 2)
            ans += 2 * huy(cur // 2)

    result = huy(n + 1) - ans // 2
    print(result)

# 示例调用
# main(10)