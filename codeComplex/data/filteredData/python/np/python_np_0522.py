import sys
from collections import deque

def build_input_from_n(n):
    # Map n to a single test instance (n_original, k, s_bytes)
    # Keep n_original = n so overall size ~ n
    if n <= 0:
        n_original = 1
    else:
        n_original = n

    # Choose k so that 1 <= k <= 10 and k <= n_original
    k = max(1, min(10, n_original))
    # Ensure k divides n_original so that original upper bound n//k is meaningful
    if n_original % k != 0:
        n_original = (n_original // k) * k
        if n_original == 0:
            n_original = k

    # Deterministic construction of s: bytes of length n_original
    # Use pattern over 'a'.. up to k letters and '?'
    chars = []
    base_letters = [97 + (i % 26) for i in range(k)]  # 'a'+i (wrap if needed)
    for i in range(n_original):
        t = i % (k + 1)
        if t == 0:
            ch = ord('?')
        else:
            ch = base_letters[(t - 1) % k]
        chars.append(ch)
    s_bytes = bytes(chars)
    return n_original, k, s_bytes

def solve(n_original, k, s):
    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (n_original + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(n_original - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0
                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                if effect[j][i] > inf:
                    effect[j][i] = inf

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n_original:
                    val = effect[j][index]
                    if val < minimum:
                        minimum = val
            minstate[state] = minimum

        return minstate[-1] <= n_original

    front = 0
    rear = n_original // k + 1
    while front < rear:
        mid = (front + rear) // 2
        if judge(mid):
            front = mid + 1
        else:
            rear = mid
    return front - 1

def main(n):
    n_original, k, s = build_input_from_n(n)
    ans = solve(n_original, k, s)
    print(ans)

if __name__ == "__main__":
    # example deterministic call
    main(100)