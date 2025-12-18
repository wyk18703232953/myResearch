import sys, string
 
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
st = []
for i in arr:
    if not st:
        st.append(i)
    else:
        while st:
            if 0 < abs(st[-1] - i) <= k:
                st.pop()
            else:
                break
        st.append(i)
print(len(st))