from collections import defaultdict

def num(s):
    l, r = 0, 0
    for i in s:
        if l == 0 and i == ")":
            r += 1
        elif i == "(":
            l += 1
        elif l and i == ")":
            l -= 1
    return (l, r)

def f(mp, cnt):
    ans = 0
    for l in cnt:
        if l.count(0) < 1:
            continue
        t = mp[l[::-1]]
        ans += t
        if t and l != l[::-1]:
            mp[l] -= 1
    return ans

def generate_string(i, n):
    # Deterministic generation of parenthesis strings based on i and n
    # Length grows with n, but remains simple and reproducible
    length = max(1, n // 2 + (i % (n + 1)))
    res = []
    for k in range(length):
        if (i + k) % 3 == 0:
            res.append("(")
        elif (i + k) % 3 == 1:
            res.append(")")

        else:
            # Alternate to keep some balance variety
            res.append("(" if (i // 2 + k) % 2 == 0 else ")")
    return "".join(res)

def main(n):
    cnt = []
    mp = defaultdict(int)
    for i in range(n):
        s = generate_string(i, n)
        l = num(s)
        cnt.append(l)
        mp[l] += 1
    result = f(mp, cnt)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)