from collections import Counter
import random

def main(n):
    # 生成测试数据：
    # 选择一个合理的 k，并生成 n 个在 [0, 2^k - 1] 范围内的整数
    # 这里令 k = max(1, n.bit_length())，保证数值范围随规模增长
    k = max(1, n.bit_length())
    max_val = (1 << k) - 1
    random.seed(0)
    a = [random.randint(0, max_val) for _ in range(n)]

    # 原始逻辑开始
    for i in range(n):
        ai = a[i]
        nai = max_val ^ ai
        if nai < ai:
            a[i] = nai

    C = Counter()
    C[0] += 1
    S = 0
    cnt = 0
    for j, ai in enumerate(a):
        nai = max_val ^ ai
        v1, v2 = C[S ^ ai], C[S ^ nai]
        if v1 <= v2:
            cnt += j + 1 - v1
            S ^= ai
            C[S] += 1
        else:
            cnt += j + 1 - v2
            S ^= nai
            C[S] += 1

    print(cnt)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(10)