def main(n):
    from collections import deque

    # Deterministic generation of k and s based on n
    # Map n to reasonable k and string length = n
    if n <= 0:
        return
    k = max(1, min(8, n))  # keep k small enough so 2^k is manageable
    # Generate a pattern with letters and '?' deterministically
    # s[i] cycles through 'a'..('a'+k-1) with some '?' injected
    chars = []
    for i in range(n):
        if i % (k + 1) == k:
            chars.append(ord('?'))
        else:
            chars.append(ord('a') + (i % k))
    s = bytes(chars)

    maxconseq = [[0 for _ in range(k)] for _ in range(n + 1)]
    for i in range(n):
        if s[i] == ord('?'):
            for j in range(k):
                maxconseq[i][j] = maxconseq[i - 1][j] + 1
        else:
            j = s[i] - 97
            maxconseq[i][j] = maxconseq[i - 1][j] + 1

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            for i in range(n - 1, -1, -1):
                if maxconseq[i][j] >= needed:
                    effect[j][i - needed + 1] = i + 1
                if effect[j][i + 1] < effect[j][i]:
                    effect[j][i] = effect[j][i + 1]

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
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    print(front - 1)


if __name__ == "__main__":
    main(1000)