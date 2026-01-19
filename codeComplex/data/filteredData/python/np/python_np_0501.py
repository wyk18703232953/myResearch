def patterns(s):
    if len(s) == 1:
        return [s, '_']
    else:
        tp = patterns(s[1:])
        return [s[0] + t for t in tp] + ['_' + t for t in tp]


def run_instance(n, m, k):
    # Deterministically generate n patterns of length k over 'a', 'b', '_'
    # Use base-3 encoding of index to generate pattern string
    def gen_pattern(idx):
        chars = []
        x = idx
        for _ in range(k):
            r = x % 3
            if r == 0:
                c = 'a'
            elif r == 1:
                c = 'b'
            else:
                c = '_'
            chars.append(c)
            x //= 3
        return ''.join(chars)

    patterns_list = [gen_pattern(i) for i in range(n)]
    ppm = {p: i for i, p in enumerate(patterns_list)}

    pre = [0] * n
    suc = [[] for _ in range(n)]

    # Deterministically generate m queries (s, ml)
    for q in range(m):
        ml = q % n
        base_str = patterns_list[ml]
        # Modify base_str deterministically based on q to form s
        s_chars = list(base_str)
        pos = (q * 7) % k
        # Flip character at pos in a deterministic way
        if s_chars[pos] == 'a':
            s_chars[pos] = 'b'
        elif s_chars[pos] == 'b':
            s_chars[pos] = 'a'
        # if '_', keep it
        s = ''.join(s_chars)

        ps = patterns(s)
        found = False
        for p in ps:
            if p in ppm:
                if ppm[p] == ml:
                    found = True
                else:
                    pre[ppm[p]] += 1
                    suc[ml].append(ppm[p])
        if not found:
            return False, []

    znodes = [i for i in range(n) if pre[i] == 0]
    res = []
    while znodes:
        i = znodes.pop()
        res.append(i + 1)
        for j in suc[i]:
            pre[j] -= 1
            if pre[j] == 0:
                znodes.append(j)
    if len(res) == n:
        return True, res
    else:
        return False, []


def main(n):
    # Map n to problem parameters:
    # - number of patterns: n
    # - pattern length k grows slowly with n using k = max(1, n.bit_length())
    # - number of constraints m = n * k (bounded by the space of possible strings)
    if n <= 0:
        print("YES")
        print()
        return

    k = max(1, n.bit_length())
    max_patterns_possible = 3 ** k
    if n > max_patterns_possible:
        n = max_patterns_possible

    m = n * k

    ok, res = run_instance(n, m, k)
    if ok:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)