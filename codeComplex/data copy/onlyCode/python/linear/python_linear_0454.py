line = input().split()
n, k = int(line[0]), int(line[1])
line = input()
if n == k:
    print(line)
 
else:
    ans = []
    arr = []
    for i in line:
        arr.append(i)
 
    for i in range(n):
        if len(ans) == k//2:
            break
        if arr[i] == '(':
            ans.append(i)
    for i in range(n-1, -1, -1):
        if len(ans) == k:
            break
        if arr[i] == ')':
            ans.append(i)
    ans.sort()
    for i in ans:
        print(arr[i], end="")