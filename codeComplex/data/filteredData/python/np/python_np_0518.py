import io
from collections import deque

def main(n):
    # Deterministically map n to original input (n, k, s)
    # Let original n = n, k = max(1, n % 8), and build s of length n
    # s pattern: cycle through 'a'..('a'+k-1) with '?' every 5th position
    orig_n = n
    k = max(1, n % 8)
    s_chars = []
    for i in range(orig_n):
        if (i + 1) % 5 == 0:
            s_chars.append('?')
        else:
            s_chars.append(chr(97 + (i % k)))
    s = "".join(s_chars).encode()

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (orig_n + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(orig_n - 1, -1, -1):
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
                if index < orig_n:
                    if effect[j][index] < minimum:
                        minimum = effect[j][index]
            minstate[state] = minimum

        return minstate[-1] <= orig_n

    front = 0
    rear = orig_n // k + 1

    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    result = front - 1
    print(result)
    return result

if __name__ == "__main__":
    main(1000)