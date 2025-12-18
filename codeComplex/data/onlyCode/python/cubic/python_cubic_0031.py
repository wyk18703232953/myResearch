s = input()
k = []
for i in range(len(s)):
    for j in range(i+1,len(s)+2):
        x = s[i:j]
        for t in range(i+1,len(s)):
            if x == s[t:t+j-i]:
                k += [j-i]
print(max(k) if k != [] else 0)