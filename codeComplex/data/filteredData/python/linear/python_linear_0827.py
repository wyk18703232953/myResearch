import random

def main(n):
    # 生成测试数据
    # q：测试组数，限制总长度大致为 n
    # 每组随机长度，和一个 k（1 <= k <= 当前串长）
    q = max(1, n // 5)  # 比如总共差不多 n 个字符量级
    test_cases = []
    remaining = n
    for _ in range(q):
        if remaining <= 0:
            break
        # 当前字符串长度在 [1, remaining] 中随机
        cur_n = random.randint(1, max(1, remaining))
        remaining -= cur_n
        # k 在 [1, cur_n]
        k = random.randint(1, cur_n)
        # 生成长度为 cur_n 的只含 R,G,B 的字符串
        S = ''.join(random.choice('RGB') for _ in range(cur_n))
        test_cases.append((cur_n, k, S))
    # 如果因为 remaining <= 0 导致没有生成任何用例，补一个最小用例
    if not test_cases:
        cur_n = max(1, n)
        k = random.randint(1, cur_n)
        S = ''.join(random.choice('RGB') for _ in range(cur_n))
        test_cases.append((cur_n, k, S))

    # 按原逻辑处理并打印答案
    for (n_i, k_i, S_str) in test_cases:
        S = list(S_str)

        for i in range(n_i):
            if S[i] == "R":
                S[i] = 0
            elif S[i] == "G":
                S[i] = 1
            else:
                S[i] = 2

        ANS = 1 << 50

        for mod in range(3):
            SUM = 0
            for i in range(k_i):
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1

            ANS = min(ANS, SUM)

            for i in range(k_i, n_i):
                if S[i - k_i] != (mod + (i - k_i)) % 3:
                    SUM -= 1
                if S[i] != (mod + i) % 3:
                    SUM += 1

                ANS = min(ANS, SUM)

        print(ANS)


if __name__ == "__main__":
    # 示例：规模 n = 50
    main(50)