from collections import deque
import random

def solve(n, k, s):
    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        # effect[j][i] = earliest position >= i where we can place a block of length `needed`
        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            # scan from right to left
            for i in range(n - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:  # 97 == ord('a')
                    accu += 1
                else:
                    accu = 0

                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                # original code had a no-op: effect[j][i] = effect[j][i+4-4]

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    minimum = min(minimum, effect[j][index])
            minstate[state] = minimum

        return minstate[-1] <= n

    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        if judge(mid):
            front = mid + 1
        else:
            rear = mid
    return front - 1


def main(n):
    # 生成参数 k（字母种类），保证 1 <= k <= 17 且 k 不大于 n
    k = max(1, min(17, n if n > 0 else 1))

    # 生成长度为 n 的测试字符串 s，由 'a'..('a'+k-1) 和 '?' 组成
    # 简单策略：每个位置随机为某个字母或 '?'
    chars = [chr(ord('a') + i) for i in range(k)] + ['?']
    s_str = ''.join(random.choice(chars) for _ in range(n))
    s_bytes = s_str.encode()  # 原逻辑中 s 是 bytes，按字节比较

    ans = solve(n, k, s_bytes)
    print(ans)