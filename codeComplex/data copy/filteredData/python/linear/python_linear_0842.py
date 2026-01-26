import sys

def solve_case(n, k, s):
    rgb = "RGB"
    ans = n
    for i in range(3):
        r = [0]
        l = i
        for c in s:
            r.append(r[-1] + (1 if c != rgb[l] else 0))
            l = (l + 1) % 3
            if len(r) > k:
                ans = min(ans, r[-1] - r[len(r) - 1 - k])
    return ans

def main(n):
    # n controls both string length and number of queries deterministically
    # define number of queries q and base string length m
    q = max(1, n)
    m = max(3, n)  # ensure length at least 3

    rgb = "RGB"

    outputs = []
    for t in range(q):
        # deterministically generate k and s from n and t
        # k in [1, m], but at most m
        k = (t % m) + 1
        # generate string s of length m using a simple pattern
        # s[i] depends deterministically on n, t and i
        s_chars = []
        for i in range(m):
            idx = (n + t + i) % 3
            s_chars.append(rgb[idx])
        s = "".join(s_chars)

        ans = solve_case(m, k, s)
        outputs.append(str(ans))

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    main(10)