import sys, string

n, m = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())
idx = -1
for i in range(n):
    if s[i] == '*':
        idx = i
if idx == -1:
    if s == t:
        print('YES')
    else:
        print('NO')
else:
    if m < n - 1:
        print('NO')
    else:
        s_left = s[0 : idx]
        s_right = s[idx + 1 : n]
        a = len(s_left)
        b = len(s_right)
        t_left = []
        t_right = []
        for i in range(a):
            t_left.append(t[i])
            t[i] = ''
        for i in range(b):
            t_right.append(t[m - i - 1])
        if s_left == t_left and s_right == t_right[::-1]:
            print('YES')
        else:
            print('NO')