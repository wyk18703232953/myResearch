import io
from collections import deque

def main(n):
    # Interpret n as the length of the string s.
    # Keep k fixed so that the algorithm structure is preserved.
    if n <= 0:
        return 0

    k = 3  # fixed alphabet size as in original usage with small k

    # Deterministic generation of s:
    # cycle through 'a'.. up to k letters, insert '?' in a pattern
    chars = [ord('a') + (i % k) for i in range(n)]
    for i in range(0, n, 5):
        chars[i] = ord('?')
    s = bytes(chars)

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

        if minstate[-1] <= n:
            return True
        return False

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


if __name__ == "__main__":
    main(30)