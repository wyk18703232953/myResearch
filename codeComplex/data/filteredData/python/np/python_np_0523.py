import io
from collections import deque

def solve(n, k, s):
    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0
        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(n - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0
                if accu >= needed:
                    index = i + needed
                effect[j][i] = index

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    if effect[j][index] < minimum:
                        minimum = effect[j][index]
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


def build_input_from_n(n):
    if n <= 0:
        n = 1
    k = max(1, n % 10 + 1)
    # ensure n is at least k for a meaningful string
    length = max(n, k)
    chars = []
    for i in range(length):
        m = i % (k + 1)
        if m == k:
            chars.append(ord('?'))
        else:
            chars.append(97 + m)
    s = bytes(chars)
    return length, k, s


def main(n):
    length, k, s = build_input_from_n(n)
    ans = solve(length, k, s)
    print(ans)


if __name__ == "__main__":
    main(10)