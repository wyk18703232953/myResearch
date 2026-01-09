def main(n):
    # 映射含义：
    # n: 数组 A 的长度
    # 生成确定性的 n, m, k, A
    # 原程序逻辑：需要 n, m, k，且 A 的元素在 1..n 范围内
    # 为保证规模可控，这里令：
    #   m = n
    #   k = max(1, n // 3)
    #   A 为严格递增序列，覆盖 1..n 中的 n 个不同位置
    if n <= 0:
        # print(0)
        pass
        return

    m = n
    k = max(1, n // 3)

    # 生成一个递增且在 [1, n] 范围内的数组 A，长度为 m=n
    # 为简单起见，直接使用 A = [1, 2, ..., n]
    A = list(range(1, n + 1))

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

    # print(ANS)
    pass
if __name__ == "__main__":
    # 示例：使用若干不同规模进行调用
    for test_n in [1, 5, 10, 50, 100]:
        main(test_n)