from collections import defaultdict, deque
from itertools import accumulate

inf = 100000000000000000  # 1e17
mod = 998244353

TRAN_dict = defaultdict(int)
TRAN_dict['_'] = 0
for i in range(97, 97 + 26):
    TRAN_dict[chr(i)] = i - 96


def cal(X):
    base = 1
    number = 0
    for x in X:
        number = number * base + TRAN_dict[x]
        base *= 27
    return number


def check(X, result, STONE):
    number = cal(X)
    if number in STONE:
        result.append(STONE[number])


def run_algorithm(n, m, k, M, S, F):
    STONE = defaultdict(int)
    for i in range(n):
        STONE[cal(list(M[i]))] = i

    bian = [[] for _ in range(n)]
    du = [0] * n

    for i in range(m):
        gain = []
        for digit in range(1 << k):
            now = list(S[i])
            tmp = bin(digit)[2:]
            tmp = '0' * (k - len(tmp)) + tmp
            for j in range(k):
                if tmp[j] == '1':
                    now[j] = '_'
            check(now, gain, STONE)
        if F[i] not in gain:
            return "NO", []
        for x in gain:
            if x != F[i]:
                bian[F[i]].append(x)
                du[x] += 1

    QUE = deque()
    for i in range(n):
        if du[i] == 0:
            QUE.append(i)
    TOP_SORT = []
    while QUE:
        now = QUE.pop()
        TOP_SORT.append(now)
        for to in bian[now]:
            du[to] -= 1
            if du[to] == 0:
                QUE.append(to)
    if len(TOP_SORT) == n:
        order = [i + 1 for i in TOP_SORT]
        return "YES", order
    else:
        return "NO", []


def generate_data(n):
    # Interpret n as the number of stones.
    # Fix k (length of strings) and m (number of constraints) as functions of n.
    # All constructions are deterministic.
    if n <= 0:
        n = 1
    k = 3
    # Limit m to be at most 2*n for scalability
    m = 2 * n

    # Generate n distinct patterns M of length k over 'a'..'z' deterministically
    # Use base-26 counting
    M = []
    for idx in range(n):
        x = idx
        chars = []
        for _ in range(k):
            chars.append(chr(ord('a') + (x % 26)))
            x //= 26
        M.append(''.join(chars))

    # Generate m constraints S and mapping F
    S = []
    F = []
    for i in range(m):
        base_pattern = M[i % n]
        chars = list(base_pattern)
        # For determinism, replace one position with '_' every few constraints
        pos = i % k
        if (i // k) % 2 == 0:
            chars[pos] = '_'
        s = ''.join(chars)
        S.append(s)
        # Map to a target index, deterministic cyclic mapping
        F.append((i * 7) % n)

    return n, m, k, M, S, F


def main(n):
    n, m, k, M, S, F = generate_data(n)
    res, order = run_algorithm(n, m, k, M, S, F)
    print(res)
    if res == "YES":
        print(*order)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)