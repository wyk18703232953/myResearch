from random import randint

mod = 10**9 + 7
d = {}
n, m, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
def go(i, j, k):
    val = i * 40401 + j * 201 + k
    ret = 0
    if val in d:
        return d[val]
    elif i < n and j < m and k < l:
        ret = max(a[i] * b[j] + go(i + 1, j + 1, k), b[j] * c[k] + go(i, j + 1, k + 1), c[k] * a[i] + go(i + 1, j, k + 1))
    elif i < n and j < m:
        ret = a[i] * b[j] + go(i + 1, j + 1, k)
    elif j < m and k < l:
        ret = b[j] * c[k] + go(i, j + 1, k + 1)
    elif k < l and i < n:
        ret = c[k] * a[i] + go(i + 1, j, k + 1)
    d[val] = ret
    return ret

a.sort(reverse = True)
b.sort(reverse = True)
c.sort(reverse = True)
print(go(0, 0, 0))
