import math
from heapq import heappush, heappop, heapify
from collections import deque
from bisect import *

rem = 10 ** 9 + 7
inf = 10 ** 18


def main(n):
    # 解释规模含义：
    # 给定 n，构造 n 个 "普通点" 和 n 个 "特殊点"，总长度为 2n
    # 对应原程序中的 n, m -> n, n
    if n <= 0:
        print()
        return

    n_val = n
    m_val = n

    total = n_val + m_val

    # 构造 arr：确定性的整数序列
    # 前 n_val 个为递增的偶数，后 m_val 个为递增的奇数
    arr = [i * 2 for i in range(total)]

    # 构造 check：前 n_val 个为 0，后 m_val 个为 1
    check = [0] * n_val + [1] * m_val

    cnt = [0 for _ in range(total)]
    left = [-1 for _ in range(total)]
    right = [-1 for _ in range(total)]

    prev = -1
    for i in range(total):
        if check[i] == 0:
            left[i] = prev
        else:
            prev = i

    prev = -1
    for i in range(total - 1, -1, -1):
        if check[i] == 0:
            right[i] = prev
        else:
            prev = i

    for i in range(total):
        if check[i] == 1:
            continue
        a = left[i]
        b = right[i]
        if a == -1 and b == -1:
            continue
        if a == -1 and b != -1:
            cnt[b] += 1
        if a != -1 and b == -1:
            cnt[a] += 1
        if a != -1 and b != -1:
            if abs(arr[i] - arr[a]) <= abs(arr[i] - arr[b]):
                cnt[a] += 1
            else:
                cnt[b] += 1

    ans = []
    for i in range(total):
        if check[i] == 1:
            ans.append(str(cnt[i]))
    print(' '.join(ans))


if __name__ == "__main__":
    # 示例调用，可按需修改 n 测试不同规模
    main(10)