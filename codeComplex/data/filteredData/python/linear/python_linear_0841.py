import sys

nxt = {'R': 'G', 'G': 'B', 'B': 'R'}

def solve_case(n, k, s):
    res = []
    for start in ['R', 'G', 'B']:
        mis = []
        cur = start
        for j in range(k):
            if s[j] != cur:
                mis.append(1)
            else:
                mis.append(0)
            cur = nxt[cur]
        res.append(sum(mis))
        for j in range(k, n):
            res.append(res[-1] + int(s[j] != cur) - mis[j - k])
            if s[j] != cur:
                mis.append(1)
            else:
                mis.append(0)
            cur = nxt[cur]
    return min(res)

def generate_string(n):
    base = ['R', 'G', 'B']
    chars = []
    for i in range(n):
        # simple deterministic but non-trivial pattern
        chars.append(base[(i * 2 + 1) % 3])
    return ''.join(chars)

def main(n):
    # interpret n as:
    # T = n (number of test cases)
    # for test t (0-based), let length = t + 1, k = max(1, (t // 2) + 1)
    # so overall total input size is O(n^2), scalable and deterministic
    T = n
    results = []
    for t in range(T):
        length = t + 1
        k = (t // 2) + 1
        if k > length:
            k = length
        s = generate_string(length)
        ans = solve_case(length, k, s)
        results.append(str(ans))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main(5)