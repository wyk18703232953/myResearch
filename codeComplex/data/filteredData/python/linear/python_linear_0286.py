from collections import defaultdict

def num(s):
    l, r = 0, 0
    for ch in s:
        if l == 0 and ch == ")":
            r += 1
        elif ch == "(":
            l += 1
        elif l and ch == ")":
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
        ans += t
        if t and l != l[::-1]:
            mp[l] -= 1
    return ans

def main(n):
    cnt = []
    mp = defaultdict(int)
    # 生成 n 个括号字符串，长度随 n 线性增长
    # 第 i 个字符串长度为 (i % 5 + 1) * max(1, n // 5)
    for i in range(n):
        length = (i % 5 + 1) * max(1, n // 5)
        # 构造确定性模式：前半部分为 '('，后半部分为 ')'
        half = length // 2
        s = "(" * half + ")" * (length - half)
        # 对部分字符串施加确定性扰动，使得有多种 (l, r) 组合
        if i % 3 == 1 and length > 2:
            s = ")" + s[1:]
        if i % 4 == 2 and length > 3:
            s = s[:-2] + "()"
        l = num(s)
        cnt.append(l)
        mp[l] += 1
    result = f(mp, cnt)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)