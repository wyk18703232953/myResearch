s = input()
n = len(s)

for L in range(n-1, 0, -1):
    if len({s[i:i+L] for i in range(n-L+1)}) < n-L+1:
        print(L)
        break
else:
    print(0)