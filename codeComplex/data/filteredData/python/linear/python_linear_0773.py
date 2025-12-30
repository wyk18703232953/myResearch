import random

def main(n: int):
    # 生成测试数据
    # 约定：m, k 与 n 同数量级，A 为严格递增的 m 个位置，范围在 [1, n]
    if n <= 0:
        print(0)
        return

    k = max(1, n // 5)          # 页面容量
    m = max(1, n // 3)          # A 的长度
    m = min(m, n)               # 不超过 n

    # 生成严格递增的 A
    positions = sorted(random.sample(range(1, n + 1), m))
    A = positions[:]            # A 是长度为 m 的递增数组

    # ================= 原逻辑开始（去掉 input） =================
    A.append(n + 1)
    COMP = []
    NOW = 0
    for a in A:
        gap = a - NOW - 1
        if gap != 0:
            if gap > 2 * k:
                COMP.append([gap % k + k, 0])
            else:
                COMP.append([gap, 0])
        COMP.append([1, 1])
        NOW = a

    COMP.pop()

    ANS = 0
    NOW_PAGE = 0
    NOW_SCORE = 0

    pa = 0
    LEN = len(COMP)
    while pa < LEN:
        i, j = COMP[pa]

        if NOW_PAGE + i <= k:
            NOW_PAGE += i
            NOW_SCORE += j
            pa += 1
        else:
            if NOW_SCORE > 0:
                COMP[pa][0] -= k - NOW_PAGE
                NOW_PAGE = k - NOW_SCORE

                ANS += 1
                NOW_SCORE = 0
            else:
                if NOW_PAGE == k:
                    NOW_PAGE = 0
                else:
                    COMP[pa][0] -= k - NOW_PAGE
                    NOW_PAGE = k - NOW_SCORE

    if NOW_SCORE > 0:
        ANS += 1

    print(ANS)


if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)