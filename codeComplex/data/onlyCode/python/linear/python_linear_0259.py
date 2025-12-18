s = input()
n = len(s)
Ans = 0
for i in range(n):
    for j in range(i + 1, n):
        L = i
        R = j
        while L < R and s[L] == s[R]:
            L += 1
            R -= 1
        if L < R and Ans < j - i + 1:
            Ans = j - i + 1
print(Ans)
