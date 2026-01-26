import sys

mod = 10**9 + 7

def count(m, n, mod):
    return (pow(2, m, mod) - 1) * pow(2, n, mod) % mod

def main(n):
    # 映射：n -> 字符串长度与查询数
    # 为了规模可控且可重复，设：
    #   字符串长度 len(S) = n
    #   查询数量 q = n
    # S 的生成：S[i] = '1' if i 为奇数 else '0'
    # 查询区间：[l, r] 采用确定性构造：
    #   l = i + 1
    #   r = min(n, i + 1 + (i % max(1, n // 3)))
    # 这样规模单调随 n 增长，且完全确定
    q = n
    S = ''.join('1' if i % 2 == 1 else '0' for i in range(n))

    LIST = [0]
    for s in S:
        if s == "1":
            LIST.append(LIST[-1] + 1)

        else:
            LIST.append(LIST[-1])

    LR = []
    span_base = max(1, n // 3)
    for i in range(q):
        l = i + 1
        r = i + 1 + (i % span_base)
        if r > n:
            r = n
        LR.append((l, r))

    for l, r in LR:
        m = LIST[r] - LIST[l - 1]
        total_len = r - l + 1
        zero_cnt = total_len - m
        # print(count(m, zero_cnt, mod))
        pass
if __name__ == "__main__":
    # 示例：使用一个固定 n 进行演示
    main(10)