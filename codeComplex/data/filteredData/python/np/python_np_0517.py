import io
import os
from collections import deque

def solve_from_params(n, k, s_bytes):
    maxconseq = [[0 for _ in range(k)] for _ in range(n + 1)]
    for i in range(n):
        if s_bytes[i] == ord('?'):
            for j in range(k):
                maxconseq[i][j] = maxconseq[i - 1][j] + 1
        else:
            j = s_bytes[i] - 97
            maxconseq[i][j] = maxconseq[i - 1][j] + 1

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0
        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            for i in range(n)[::-1]:
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

        if minstate[-1] <= n:
            return True
        return False

    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid
    return front - 1


def main(n):
    if n < 1:
        print(0)
        return
    k = (n % 5) + 1
    chars = []
    for i in range(n):
        r = i % (k + 1)
        if r == k:
            chars.append('?')
        else:
            chars.append(chr(97 + r))
    s = ''.join(chars).encode()
    ans = solve_from_params(n, k, s)
    print(ans)


if __name__ == "__main__":
    main(10)