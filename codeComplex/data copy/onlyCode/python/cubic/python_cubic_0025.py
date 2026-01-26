# http://codeforces.com/problemset/problem/23/A
leng = 0
s = input()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if s.count(sub) >= 2 and len(sub) > leng:
            leng = len(sub)
        elif s.count(sub) == 1:
            for k in range(1, len(sub)):
                if s[i - k:j - k] == sub and len(sub) > leng:
                    leng = len(sub)
print(leng)

