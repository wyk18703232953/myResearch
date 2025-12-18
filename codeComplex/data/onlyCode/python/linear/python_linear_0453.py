import sys, string

n, k = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().rstrip())
st = []
ans = []
for i in range(n):
    if k <= 0:
        break
    else:
        if arr[i] == '(':
            st.append((arr[i], i))
        else:
            if st and st[-1][0] == '(':
                k -= 2
                ans.append(st.pop())
                ans.append((arr[i], i))
            else:
                st.append((arr[i], i))

ans.sort(key=lambda x: x[1])
res = []
for i in ans:
    res.append(i[0])
print(''.join(res))