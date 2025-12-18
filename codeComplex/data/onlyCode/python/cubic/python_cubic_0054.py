s = input()
sLen, ans = len(s), 0

for i in range(sLen - 1):
    for till1 in range(i + 1, sLen):
        till2 = till1 + 1
        for j in range(i + 1, sLen):
            if till2 > sLen:
                break;
            sub1 = s[i:till1]
            sub2 = s[j:till2]
            subLen = len(sub1)
            if sub1 == sub2 and subLen > ans:
                ans = subLen
            till2 += 1

print(ans)
