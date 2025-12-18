n = int(input())
s = input()
t = input()
pair2ind = {}
letters_s = [0] * 26
letters_t = [0] * 26
non_common = set()
cnt = 0
for i in range(n):
    if s[i] != t[i]:
        pair2ind[(s[i], t[i])] = i + 1
        letters_s[ord(s[i]) - ord('a')] = i + 1
        letters_t[ord(t[i]) - ord('a')] = i + 1
        non_common.add(i + 1)
        cnt += 1

sim = -1
for i in range(26):
    if letters_s[i] != 0 and letters_t[i] != 0:
        sim = letters_s[i]
        break
else:
    print(cnt)
    print(-1, -1)
    exit()

for i in range(n):
    if s[i] != t[i]:
        if (t[i], s[i]) in pair2ind:
            print(cnt - 2)
            print(pair2ind[(s[i], t[i])], pair2ind[(t[i], s[i])])
            exit()

non_common.remove(sim)
print(cnt - 1)
print(sim, letters_t[ord(s[sim-1]) - ord('a')])
exit()
