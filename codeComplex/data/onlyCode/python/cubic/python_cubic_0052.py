S = input()
sLen, ans = len(S), 0
for i in range(sLen):
    for till1 in range(i + 1, sLen):
        till2 = till1 + 1
        for j in range(i + 1, sLen):
            if till2 > sLen:
                break
            sub1 = S[i:till1]
            sub2 = S[j:till2]
            subLen = len(sub1)
            if sub1 == sub2 and ans < subLen:
                ans = subLen
            till2 += 1

print(ans)
