def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
a = li()
lf = [(a[i], i) for i in range(n) if a[i] == 1]
it = [(a[i], i) for i in range(n) if a[i] > 1]
it.sort(reverse=True)
while len(lf) < 2:
    lf.append(it.pop())

ed = []
_, last = lf.pop()

for i in range(len(it)):
    cap, u = it[i]
    if i != 0:
        ed.append((it[i - 1][1], u))
        cap -= 1
    while lf and cap > 1:
        _, l = lf.pop()
        ed.append((u, l))
        cap -= 1

if lf:
    ans = 'NO'
else:
    ans = 'YES %d' % (len(it) + 1,)
    ed.append((it[-1][1], last))
    ans1 = str(len(ed))
    ans2 = '\n'.join('%d %d' % (u + 1, v + 1) for u, v in ed)
    ans = '\n'.join([ans, ans1, ans2])
print(ans)
