n, k =map(int,input().split())
a = list(map(int, input().split()))
if n == 1:
    print(a[0])
    print(1)
else:
    lst = sorted(a)[-k:]
    ans = sum(lst)
    print(ans)
    c = 0
    ln = len(lst)
    ans = [0]
    cnt = 0
    for i in range(n):
        if cnt == k - 1:
            break
        for j in range(ln):
            if a[i] == lst[j]:
                lst[j] = -1
                ans.append(i + 1)
                cnt += 1
                break
    ln = len(ans)
    for i in range(1,ln):
        print(ans[i] - ans[i - 1], end = " ")
    print(n - ans[-1])


