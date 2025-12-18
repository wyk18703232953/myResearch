w, h, n = map(int, input().split())
l, r = [-1] * (w+1), [-1] * (w+1)
t, b = [-1] * (h+1), [-1] * (h+1)
l[0], b[0], t[h], r[w] = 0, 0, h, w
V, H = [0] * n, [0] * n

for i in range(n):
    line, idx = input().split()
    idx = int(idx)
    if line == 'V':
        r[idx] = w
        V[i] = idx
    else:
        t[idx] = h
        H[i] = idx

left, max_w = 0, 0
for i in range(1, w+1):
    if r[i] != -1:
        l[i] = left
        r[left] = i
        max_w = max(max_w, i - left)
        left = i

bottom, max_h = 0, 0
for i in range(1 ,h+1):
    if t[i] != -1:
        b[i] = bottom
        t[bottom] = i
        max_h = max(max_h, i - bottom)
        bottom = i

res = [0] * n
res[n-1] = max_h * max_w
for i in range(n-1, 0, -1):
    if V[i] != 0:
        max_w = max(max_w, r[V[i]] - l[V[i]])
        r[l[V[i]]] = r[V[i]]
        l[r[V[i]]] = l[V[i]]
    else:
        max_h = max(max_h, t[H[i]] - b[H[i]])
        b[t[H[i]]] = b[H[i]]
        t[b[H[i]]] = t[H[i]]
    res[i-1] = max_h * max_w

for i in range(n):
    print(res[i])