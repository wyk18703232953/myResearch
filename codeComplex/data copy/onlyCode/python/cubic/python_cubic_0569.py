from collections import Counter
a = input()
b = input()
if len(a) < len(b):
    print(''.join(sorted(a)[::-1]))
    exit()
n = len(a)
cnt = Counter(a)
def f(i = 0, check = False):
    if i == n: return []
    for j in sorted(cnt)[::-1]:
        if (check or j <= b[i]) and cnt[j]:
            cnt[j] -= 1
            res = f(i + 1, check or j < b[i])
            if len(res) + i + 1 == n:
                res.append(j)
                return res
            cnt[j] += 1
    return []
print(''.join(f()[::-1]))