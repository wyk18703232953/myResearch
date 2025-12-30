from collections import deque
import random

def main(n):
    # 生成测试数据：随机选择 k，并生成长度为 n 的字符串 s，字符为 'a'..('a'+k-1) 或 '?'
    if n <= 0:
        return 0

    # 1 <= k <= min(5, n)（可按需要调整上界）
    k = random.randint(1, min(5, n))

    # 随机生成字符串 s
    chars = [chr(ord('a') + i) for i in range(k)] + ['?']
    s_str = ''.join(random.choice(chars) for _ in range(n))
    s = s_str.encode()  # 原程序按字节处理，用 ord 比较

    # 预处理 maxconseq，逻辑与原程序一致
    maxconseq = [[0 for _ in range(k)] for _ in range(n + 1)]
    for i in range(n):
        if s[i] == ord('?'):
            for j in range(k):
                # 连续问号也可以接在任何字母后
                maxconseq[i][j] = maxconseq[i - 1][j] + 1
        else:
            j = s[i] - 97  # ord('a') == 97
            maxconseq[i][j] = maxconseq[i - 1][j] + 1

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        # effect[j][i] 表示：从位置 i 开始，最早能结束一个长度为 needed 的字母 j 段的下一个位置
        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            for i in range(n - 1, -1, -1):
                if maxconseq[i][j] >= needed:
                    effect[j][i - needed + 1] = i + 1
                effect[j][i] = min(effect[j][i], effect[j][i + 1])

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

    # 二分答案，与原逻辑一致
    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        if judge(mid):
            front = mid + 1
        else:
            rear = mid

    ans = front - 1
    print(ans)
    return ans