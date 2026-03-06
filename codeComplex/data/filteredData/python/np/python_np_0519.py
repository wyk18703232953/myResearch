def main(n):
    # Scale interpretation:
    # n controls the string length; k is fixed small to keep bitmask DP meaningful.
    # We choose k=3 deterministically and build a string s of length n.
    k = 3
    if n < k:
        s = b"a" * n
    else:
        # Deterministic pattern using 'a','b','c','?'
        base_chars = [ord('a') + (i % k) for i in range(n)]
        # Insert '?' periodically in a deterministic way
        s_list = []
        for i, ch in enumerate(base_chars):
            if i % (k + 1) == 0:
                s_list.append(ord('?'))
            else:
                s_list.append(ch)
        s = bytes(s_list)

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
                effect[j][i] = effect[j][i + 4 - 4]

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    val = effect[j][index]
                    if val < minimum:
                        minimum = val
            minstate[state] = minimum

        return minstate[-1] <= n

    front = 0
    rear = n // k + 1

    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    result = front - 1
    print(result)


if __name__ == "__main__":
    main(1000)