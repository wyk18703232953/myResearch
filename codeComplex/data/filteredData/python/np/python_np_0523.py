from collections import deque
import random
import string


def solve(n, k, s):
    # original judge() function, adapted to Python string `s`
    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (n + 1) for _ in range(k)]

        # precompute for each character j and position i the earliest index
        # where a segment of length `needed` ending at/after i is possible
        for j in range(k):
            accu = 0
            index = inf
            for i in range(n - 1, -1, -1):
                if s[i] == '?' or s[i] == chr(97 + j):
                    accu += 1
                else:
                    accu = 0

                if accu >= needed:
                    index = i + needed
                effect[j][i] = index

        # DP over subsets of characters
        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    minimum = min(minimum, effect[j][index])
            minstate[state] = minimum

        return minstate[-1] <= n

    # binary search maximum feasible `needed`
    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        if judge(mid):
            front = mid + 1
        else:
            rear = mid
    return front - 1


def generate_test_string(n, k):
    # generate a random test string of length n over 'a'..'a'+k-1 and '?'
    chars = [chr(97 + i) for i in range(k)]
    chars.append('?')
    return ''.join(random.choice(chars) for _ in range(n))


def main(n):
    # choose k based on n (ensure k >= 1 and not too large)
    k = max(1, min(10, n if n > 0 else 1))
    s = generate_test_string(n, k)
    # for debugging, you might want to inspect s/k here
    result = solve(n, k, s)
    print(result)