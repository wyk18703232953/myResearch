def main(n):
    from collections import deque

    # Map n to original problem parameters:
    # Original had: n (length of string), k (alphabet size), s (string with '?' and 'a'+j).
    # Here we choose:
    #   k = max(1, min(8, n))       (bounded to keep 2^k states reasonable)
    #   length = n                  (string length)
    # Deterministic string construction:
    #   s[i] cycles through '?' and 'a'..'a'+k-1 in a fixed pattern.
    k = max(1, min(8, n if n > 0 else 1))
    length = max(1, n)

    pattern = ['?'] + [chr(97 + (i % k)) for i in range(k)]
    pat_len = len(pattern)
    chars = [pattern[i % pat_len] for i in range(length)]
    s = bytes(''.join(chars), 'ascii')

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (length + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(length - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0

                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                if effect[j][i + 4 - 4] < effect[j][i + 3 - 3]:
                    effect[j][i] = effect[j][i + 4 - 4]
                else:
                    effect[j][i] = effect[j][i + 3 - 3]

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < length:
                    if effect[j][index] < minimum:
                        minimum = effect[j][index]
            minstate[state] = minimum

        if minstate[-1] <= length:
            return True
        return False

    front = 0
    rear = length // k + 1

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