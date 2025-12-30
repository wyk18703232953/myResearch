from itertools import accumulate
import bisect
import random

def main(n):
    # 生成测试数据
    # A: 长度为 n 的正整数数组
    A = [random.randint(1, 10) for _ in range(n)]
    # q: 查询次数，这里设为 n
    q = n
    # K: 长度为 q 的正整数数组
    K = [random.randint(1, 10) for _ in range(q)]

    # 原逻辑
    C = [0] + A
    C = list(accumulate(C))
    total = 0
    ans = [0] * q

    for i, k in enumerate(K):
        total += k
        j = bisect.bisect_right(C, total)
        if j != n + 1:
            ans[i] = n - (j - 1)
        else:
            ans[i] = n
            total = 0

    print(*ans, sep='\n')

if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)