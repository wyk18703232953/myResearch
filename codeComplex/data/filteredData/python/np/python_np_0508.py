def get_hash(s):
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

def main(n):
    # Map n to problem parameters deterministically
    # Keep k small to avoid 30**k blowup
    k = 3
    # Number of patterns
    num_patterns = max(1, n)
    # Number of constraints/edges
    m = num_patterns

    # Deterministically generate pattern strings of length k
    # Characters from 'a'..'z'
    patterns = []
    for i in range(num_patterns):
        s = []
        for j in range(k):
            # deterministic char based on i and j
            c = chr(ord('a') + (i + j) % 26)
            s.append(c)
        patterns.append("".join(s))

    # pattern_pos array as in original code
    pattern_pos = [-1] * (30 ** k)
    for i, p in enumerate(patterns):
        h = get_hash(p)
        pattern_pos[h] = i + 1

    # Generate m constraints (s, l)
    # s is a k-length string, l is in [1, num_patterns]
    s_list = []
    l_list = []
    for i in range(m):
        base_idx = i % num_patterns
        l = (i % num_patterns) + 1
        # generate s by taking pattern[base_idx] and toggling some positions to '_'
        base = patterns[base_idx]
        chars = list(base)
        mask = i % (2 ** k)
        for j in range(k):
            if mask & (1 << j):
                chars[j] = '_'
        s = "".join(chars)
        s_list.append(s)
        l_list.append(l)

    from collections import defaultdict

    parents = [0] * (num_patterns + 1)
    edges = defaultdict(list)
    failed = False

    for s, l in zip(s_list, l_list):
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
    for i in range(1, num_patterns + 1):
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

    if len(ans) == num_patterns:
        print('YES')
        print(*ans)
    else:
        print('NO')

if __name__ == "__main__":
    main(10)