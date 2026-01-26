# TC - O(n)
#SC - O(n)
size = int(input())
s = input()


ct = 0
F = 0
for i in range(size-2):
    if s[i]==s[i+1] and s[i+1]==s[i+2] and s[i] == 'x':
        ct += 1
        F = 1

if F == 0:
    print(0)
else:
    print(ct)