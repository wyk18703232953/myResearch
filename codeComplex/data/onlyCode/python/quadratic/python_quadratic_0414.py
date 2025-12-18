n, k = map(int, input().split())
s = input()
# fail = [-1] * len(s)
# for i in range(1, len(s)):
#     j = fail[i - 1]
#     while j != -1 and s[i - 1] != s[j]:
#         j = fail[j]
#     fail[i] = j + 1
# # print(fail)
# l = fail[-1]
# print(s + s[l:] * (k - 1))
for i in range(1, n):
    if s[:n - i] == s[i:]:
        print(s + s[n - i:] * (k - 1))
        exit()
print(s * k)
