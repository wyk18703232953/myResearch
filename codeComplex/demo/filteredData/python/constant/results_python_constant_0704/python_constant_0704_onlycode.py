s = map(int, raw_input().rstrip().split())
n = s[0]
v = s[1]

primo = min(n -1, v)
if primo == n-1:
    print(primo)
else:
    rimane = n - primo
    print(primo - 1 + (rimane)*(rimane + 1) / 2)