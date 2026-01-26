n = int(input())
s = list(input())
t = input()
if sorted(s) != sorted(t):
    print(-1)
else:
    lst = [0] * n
    for i in range(n):
        for j in range(n):
            if s[j] == t[i]:
                lst[j] = i + 1
                s[j] = "."
                break
    ans = 0
    a = []
    for i in range(n):
        for j in range(n - 1):
            if i != j:
                if lst[j] > lst[j + 1]:
                    ans += 1
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    a.append(j+1)
    print(ans)
    print(*a)