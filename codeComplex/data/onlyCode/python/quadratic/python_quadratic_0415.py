n, k = map(int, input().split())
s = input()
fail = [-1] * (len(s) + 1)
for i in range(1, len(s) + 1):
    j = fail[i - 1]
    while j != -1 and s[i - 1] != s[j]:
        j = fail[j]
    fail[i] = j + 1
# print(fail)

f1 = fail[-1]
print(s + s[f1:] * (k - 1))