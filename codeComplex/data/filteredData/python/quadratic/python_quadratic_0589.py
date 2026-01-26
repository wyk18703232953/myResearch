def gen(n, b):
    a = [(x + b) % 3 for x in range(n)]
    s = ""
    for i in range(n):
        if a[i] == 0:
            s += "R"
        if a[i] == 1:
            s += "G"
        if a[i] == 2:
            s += "B"
    return s


def solve_single(n, k, s):
    ans = n
    for xi in range(3):
        t = gen(n, xi)
        diff = 0
        for i in range(k):
            if s[i] != t[i]:
                diff += 1
        ans = min(ans, diff)
        for j in range(k, n):
            if s[j - k] != t[j - k]:
                diff -= 1
            if s[j] != t[j]:
                diff += 1
            ans = min(ans, diff)
    return ans


def generate_case(case_id, n):
    if n <= 0:
        return 0, 0, ""
    k = max(1, n // 2)
    base_pattern = gen(n, case_id % 3)
    s_list = []
    for i, ch in enumerate(base_pattern):
        if (i + case_id) % 5 == 0:
            if ch == "R":
                s_list.append("G")
            elif ch == "G":
                s_list.append("B")

            else:
                s_list.append("R")

        else:
            s_list.append(ch)
    s = "".join(s_list)
    return n, k, s


def main(n):
    if n <= 0:
        return []
    q = max(1, n // 5)
    results = []
    for case_id in range(q):
        nn, kk, ss = generate_case(case_id, n)
        res = solve_single(nn, kk, ss)
        results.append(res)
    return results


if __name__ == "__main__":
    # example call
    out = main(10)
    for v in out:
        # print(v)
        pass