n = int(input())
s = input()
t = input()
p = [-1, -1]
a = [[-1] * 26 for i in range(26)]
k = 0
for i in range(n):
    if t[i] != s[i]:
        k += 1
for i in range(n):
    if t[i] != s[i]:
        if a[ord(t[i]) - 97][ord(s[i]) - 97] != -1:
            print(k - 2)
            print(a[ord(t[i]) - 97][ord(s[i]) - 97] + 1, i + 1)
            exit()
        a[ord(s[i]) - 97][ord(t[i]) - 97] = i
for i in range(n):
    if t[i] != s[i]:
        for j in range(26):
            if a[j][ord(s[i]) - 97] != -1:
                print(k - 1)
                print(a[j][ord(s[i]) - 97] + 1, i + 1)
                exit()
        a[ord(s[i]) - 97][ord(t[i]) - 97] = i
print(k)
print(-1, -1)
