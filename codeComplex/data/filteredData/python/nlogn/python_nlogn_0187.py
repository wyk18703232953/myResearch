from collections import defaultdict
import random


def main(n: int):
    # 1. 生成规模为 n 的测试数据 A
    # 这里随机构造整数数组，可按需要修改范围
    A = [random.randint(0, 10**9) for _ in range(n)]

    # 2. 原逻辑实现
    N = n
    sum_A = sum(A)
    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1

    ans = 0
    for i in range(N):
        a = A[i]
        cnt[a] -= 1
        sum_A -= a

        tmp = sum_A
        same_or_adjacent_count = 0
        for b in (a - 1, a, a + 1):
            same_or_adjacent_count += cnt[b]
            tmp -= b * cnt[b]
        ans += tmp - a * (N - 1 - i - same_or_adjacent_count)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)