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
        if l != (0, 0) and l == l[::-1]:
            continue
        t = mp[l[::-1]]
        t2 = mp[l[::-1]]
        ans += t
        if t and l != l[::-1]:
            mp[l] -= 1
    return ans

def generate_string(k):
    # Deterministically generate a parenthesis string of length k
    # pattern: first half '(', second half ')'
    # if k is odd, last char is '('
    half = k // 2
    s = "(" * half + ")" * half
    if len(s) < k:
        s += "("
    return s

def main(n):
    cnt = []
    mp = defaultdict(int)
    # Interpret n as the number of strings; length of each string is n as well
    for i in range(n):
        s = generate_string(n + i)
        l = num(s)
        cnt.append(l)
        mp[l] += 1
    result = f(mp, cnt)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)