from math import *

def main(n):
    # 解释规模含义：
    # n -> 原程序中的 n（数组长度），k 固定为 3（可按需调整为其他常数）
    if n <= 0:
        # print(0)
        pass
        return

    k = 3
    lul = 2 ** k - 1  # 全 1 掩码

    # 确定性数据生成：A[i] = (i * 2 + 1) & lul
    A = [((i * 2 + 1) & lul) for i in range(n)]

    ans = [0] * n
    ans[0] = A[0]
    for j in range(1, n):
        ans[j] = ans[j - 1] ^ A[j]

    d = dict()
    for j in range(n):
        if ans[j] in d:
            d[ans[j]] += 1

        else:
            d[ans[j]] = 1

    total_ans = 0

    def huy(x):
        return x * (x - 1) // 2

    for j in d:
        now = d[j]
        xor = lul ^ j
        cur = now

        if xor in d:
            now2 = d[xor]
            cur += now2

            total_ans += huy(cur // 2 + cur % 2)
            total_ans += huy(cur // 2)
            if j == 0:
                total_ans += 2 * (cur // 2)

        else:
            if j == 0 or xor == 0:
                total_ans += 2 * (cur // 2)
            total_ans += 2 * huy(cur // 2 + cur % 2)
            total_ans += 2 * huy(cur // 2)

    # print(huy(n + 1) - total_ans // 2)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行时间复杂度实验
    main(10)