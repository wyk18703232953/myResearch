from collections import deque
import random


def main(n):
    # 随机生成参数 k（1 到 10，且 k <= n）
    k = random.randint(1, min(10, n))

    # 随机生成长度为 n 的字符串 s，只包含 'a'..('a'+k-1) 和 '?'
    alphabet = [chr(ord('a') + i) for i in range(k)]
    choices = alphabet + ['?']
    s_chars = [random.choice(choices) for _ in range(n)]
    s = "".join(s_chars).encode()  # 原逻辑基于字节串

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (n + 1) for _ in range(k)]

        # 预处理每个字母 j 在每个位置 i 之后，若要放长度为 needed 的连续段，
        # 最早能结束的位置 index
        for j in range(k):
            accu = 0
            index = inf
            for i in range(n - 1, -1, -1):
                if s[i] == ord(b'?') or s[i] == (97 + j):
                    accu += 1
                else:
                    accu = 0

                if accu >= needed:
                    index = i + needed
                effect[j][i] = index

        # 动态规划：状态为已经覆盖了哪些字母
        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (state & (1 << j)) == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    minimum = min(minimum, effect[j][index])
            minstate[state] = minimum

        return minstate[-1] <= n

    # 二分答案
    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        if judge(mid):
            front = mid + 1
        else:
            rear = mid

    # 保持原程序的行为：输出最大可行长度
    print(front - 1)


if __name__ == "__main__":
    # 示例：可在此处调整规模
    main(100)