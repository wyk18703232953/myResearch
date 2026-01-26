def solve2(s, t, left, right):
    n = len(s)
    m = len(t)
    nuxt = [-1] * (left + 1)
    nuxt[0] = 0

    for i in range(n):
        for j in reversed(range(left + 1)):
            k = nuxt[j]
            if k == -1:
                continue
            if j != left:
                if s[i] == t[j]:
                    nuxt[j + 1] = max(nuxt[j + 1], k)
            if k != right:
                if s[i] == t[left + k]:
                    nuxt[j] = max(nuxt[j], k + 1)
    return nuxt[-1] == right

def run_case(s, t):
    m = len(t)
    for i in range(m + 1):
        if solve2(s, t, i, m - i):
            return "YES"
    return "NO"

def main(n):
    t = max(1, n)
    results = []
    for i in range(1, t + 1):
        len_s = max(1, i)
        len_t = max(1, i // 2 + 1)
        s = "".join(chr(ord('a') + (j % 26)) for j in range(len_s))
        t_str = "".join(chr(ord('a') + ((j * 3 + 1) % 26)) for j in range(len_t))
        res = run_case(s, t_str)
        results.append(res)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)