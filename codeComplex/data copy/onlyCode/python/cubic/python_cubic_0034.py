S = input()

ans = 0
met = set()

for i in range(len(S)):
    for j in range(i, -1, -1):
        if S[j:i+1] in met:
            ans = max(ans, i - j + 1)
        else:
            met.add(S[j:i+1])
            
print(ans)