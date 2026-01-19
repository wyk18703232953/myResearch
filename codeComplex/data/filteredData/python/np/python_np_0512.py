from collections import defaultdict, deque

inf = 100000000000000000  # 1e17
mod = 998244353


def build_deterministic_input(n):
    if n <= 0:
        n = 1
    # k is pattern length, keep small and fixed for clarity
    k = 3
    # number of stones
    num_stones = n
    # number of patterns/constraints
    num_patterns = n

    # build M: list of stone strings, each of length k
    # deterministic construction using letters 'a'..'z' and '_'
    chars = [chr(ord('a') + i) for i in range(26)]
    M = []
    for i in range(num_stones):
        s = []
        x = i
        for _ in range(k):
            s.append(chars[x % 26])
            x //= 26
        M.append("".join(s))

    # build patterns S and target indices F
    # For i-th pattern, take M[i % num_stones] as base, then
    # deterministically turn some positions into '_' in S,
    # and choose F so that it is always reachable.
    S = []
    F = []
    for i in range(num_patterns):
        base_idx = i % num_stones
        base = list(M[base_idx])
        pat = base[:]
        for j in range(k):
            if ((i + j) % 3) == 0:
                pat[j] = '_'
        S.append("".join(pat))
        F.append(base_idx)
    return num_stones, num_patterns, k, M, S, F


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


def main(n):
    n, m, k, M, S, F = build_deterministic_input(n)

    STONE = defaultdict(int)
    for i in range(n):
        STONE[cal(list(M[i]))] = i

    def check(X, result):
        number = cal(X)
        if number in STONE:
            result.append(STONE[number])

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
            check(now, gain)
        if F[i] not in gain:
            print("NO")
            return
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
        print("YES")
        print(*[i + 1 for i in TOP_SORT])
    else:
        print("NO")


if __name__ == "__main__":
    main(10)