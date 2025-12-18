from sys import stdin
from collections import Counter

rstr = lambda: stdin.readline().strip()
a, b = list(rstr()), list(rstr())

if len(a) < len(b) or len(a) == 1:
    print(''.join(sorted(a)[::-1]))
else:
    ans, tem = 0, []

    for i in range(len(b)):
        for j in range(int(b[i]) - 1, -1, -1):
            if str(j) in a and not (j == i == 0):
                a.remove(str(j))
                ans = max(ans, int(''.join(tem) + str(j) + ''.join(sorted(a)[::-1])))
                a.append(str(j))
                break

        if b[i] not in a:
            break

        tem.append(b[i])
        a.remove(b[i])
        
    if tem:
        ans = max(ans, int(''.join(tem)))

    print(ans)
