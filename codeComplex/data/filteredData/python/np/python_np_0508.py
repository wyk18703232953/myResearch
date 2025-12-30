from collections import defaultdict
import random
import string

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

def generate_random_pattern(k):
    # patterns consist of lowercase letters and underscores
    chars = string.ascii_lowercase + '_'
    return ''.join(random.choice(chars) for _ in range(k))

def generate_random_s(k):
    # s strings consist of lowercase letters, no underscores (since matches uses ord(c)-96)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(k))

def main(n):
    # scale parameter: n = number of patterns
    # choose k small enough to keep 30**k manageable; here fixed k=3
    k = 3

    # number of edges (queries)
    # here choose m proportional to n, but you can change this policy
    m = max(1, n * 2)

    # generate n distinct patterns of length k
    patterns = set()
    pattern_list = []
    while len(pattern_list) < n:
        p = generate_random_pattern(k)
        if p not in patterns:
            patterns.add(p)
            pattern_list.append(p)

    # initialize pattern_pos
    pattern_pos = [-1] * (30 ** k)
    for i, p in enumerate(pattern_list):
        h = get_hash(p, k)
        pattern_pos[h] = i + 1  # patterns indexed from 1

    # generate m (s, l) pairs
    # l must be in [1, n]
    queries = []
    for _ in range(m):
        s = generate_random_s(k)
        l = random.randint(1, n)
        queries.append((s, l))

    parents = [0] * (n + 1)
    edges = defaultdict(list)
    failed = False

    for s, l in queries:
        M = matches(s, k, pattern_pos)
        if l in M:
            for m_id in M:
                if l == m_id:
                    continue
                edges[l].append(m_id)
                parents[m_id] += 1
        else:
            failed = True
            break

    if failed:
        print('NO')
        return

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
        print('YES')
        print(*ans)
    else:
        print('NO')


if __name__ == "__main__":
    # example run with n = 5
    main(5)