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

def main(n):
    # 生成 n 个确定性的括号串
    # 第 i 个串长度为 i % 10 + 1，模式在几种构造之间切换
    strings = []
    for i in range(1, n + 1):
        length = i % 10 + 1
        typ = i % 4
        if typ == 0:
            s = "(" * length
        elif typ == 1:
            s = ")" * length
        elif typ == 2:
            half = length // 2
            s = "(" * half + ")" * (length - half)

        else:
            s = ")" * (length // 2) + "(" * (length - length // 2)
        strings.append(s)

    cnt = []
    mp = defaultdict(int)
    for s in strings:
        l = num(s)
        cnt.append(l)
        mp[l] += 1

    result = f(mp, cnt)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)