import sys
from collections import defaultdict

def get_hash(s, k):
    r = 0
    for c in s:
        r *= 30
        if c != '_':
            r += ord(c) - 96
    return r

def matches(s, k, pattern_pos):
    R = []
    for i in range(2 ** k):
        r = 0
        for j in range(k):
            if i & (1 << j):
                r += (ord(s[j]) - 96) * (30 ** (k - j - 1))
        if pattern_pos[r] >= 0:
            R.append(pattern_pos[r])
    return R

def generate_data(n):
    # Map n to problem size:
    # number of patterns = n
    # k (pattern length) grows slowly with n so 30**k stays reasonable
    # number of edges m ~ n
    if n < 1:
        n = 1
    k = 3 if n < 20 else 4
    m = n

    # generate n distinct patterns of length k over 'a'..'z' and '_'
    alphabet = [chr(ord('a') + i) for i in range(26)] + ['_']
    patterns = []
    for i in range(n):
        s_chars = []
        x = i
        for pos in range(k):
            idx = (x + pos) % len(alphabet)
            s_chars.append(alphabet[idx])
            x //= 2
        patterns.append(''.join(s_chars))

    # generate m constraints (s, l)
    # l in [1..n], s derived deterministically from pattern[l-1] and index i
    constraints = []
    for i in range(m):
        l = (i % n) + 1
        base = patterns[l - 1]
        s_list = list(base)
        # tweak characters in a deterministic pattern
        if k >= 1:
            s_list[0] = alphabet[(alphabet.index(s_list[0]) + (i % 3)) % len(alphabet)]
        if k >= 2:
            s_list[1] = alphabet[(alphabet.index(s_list[1]) + (i % 5)) % len(alphabet)]
        s = ''.join(s_list)
        constraints.append((s, l))

    return n, m, k, patterns, constraints

def core_logic(n, m, k, patterns, constraints):
    pattern_pos = [-1] * (30 ** k)
    for i in range(n):
        p = get_hash(patterns[i], k)
        pattern_pos[p] = i + 1

    parents = [0] * (n + 1)
    edges = defaultdict(list)
    failed = False

    for s, l in constraints:
        M = matches(s, k, pattern_pos)
        if l in M:
            for mm in M:
                if l == mm:
                    continue
                edges[l].append(mm)
                parents[mm] += 1
        else:
            failed = True
            break

    if failed:
        return False, []

    Q = []
    for i in range(1, n + 1):
        if parents[i] == 0:
            Q.append(i)

    ans = []
    while Q:
        i = Q.pop()
        ans.append(i)
        for child in edges[i]:
            parents[child] -= 1
            if parents[child] == 0:
                Q.append(child)

    if len(ans) == n:
        return True, ans
    else:
        return False, []

def main(n):
    n, m, k, patterns, constraints = generate_data(n)
    ok, order = core_logic(n, m, k, patterns, constraints)
    if ok:
        print('YES')
        print(*order)
    else:
        print('NO')

if __name__ == "__main__":
    main(10)