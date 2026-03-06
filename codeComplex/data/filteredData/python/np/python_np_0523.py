def main(n):
    from collections import deque

    # Map n to problem parameters:
    # Let original n_str_len = n, and k derived deterministically from n
    # Ensure k >= 1 and not too large; use k between 1 and 7 for scalability
    if n <= 0:
        return
    k = max(1, min(7, n % 7 + 1))
    orig_n = n

    # Deterministic generation of s as bytes:
    # Use pattern of 'a' + (i % k) and '?' at positions divisible by (k+1)
    s_chars = []
    for i in range(orig_n):
        if (i % (k + 1)) == 0:
            s_chars.append(ord('?'))
        else:
            s_chars.append(ord(97 + (i % k)))
    s = bytes(s_chars)

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

    print(front - 1)


if __name__ == "__main__":
    main(1000)