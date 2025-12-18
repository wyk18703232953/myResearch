import collections
n = int(input())
s = input()
t = input()
if collections.Counter(s) != collections.Counter(t):
    print(-1)
    exit()
sl = list(s)
st = list(t)
ans = []
p = 0
while sl:
    if sl[0] != st[0]:
        k = sl.index(st[0])
        ans.extend(list(range(k + p, p, -1)))
        sl.pop(k)
        st.pop(0)

    else:
        sl.pop(0)
        st.pop(0)
    p += 1
print(len(ans))
print(*ans)
