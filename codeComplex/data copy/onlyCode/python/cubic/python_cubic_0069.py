'''
s = input()
for i in range(len(s)):

    for k in range(i + 1, len(s)+1, 1):
        print(s[i:k])
'''
'''
s = input()
sLen = len(s)
for startInd in range(sLen):
    for endInd in range(startInd + 1, sLen + 1):
        print(s[startInd, endInd])

'''
s = input()
slen = len(s)
ans = 0
for st1 in range(slen - 1):
    for end1 in range(st1 + 1, slen):
        end2 = end1 + 1
        sub1 = s[st1:end1]
        for st2 in range(st1 + 1, slen):
            if end2 > slen:
                break

            sub2 = s[st2:end2]
            subLen = len(sub1)
            if sub1 == sub2 and ans < subLen:
                ans = subLen
            end2 += 1

print(ans)
