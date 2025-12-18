'''
s = input()
sLen = len(s)
while sLen != 0:
    for i in range(sLen):
        print(s[i])
        sLen = sLen - 1
'''

'''
   012345
s='abcdef'
s[0:1] =='a'
s[0:2]=='ab'
........
s[1:2]=='b'
s[1:3]=='bc'
s[1:4]=='bcd'
.......
s[2:3]=='c'
s[2:4]=='cd'
......
'''
s = input()
sLen, ans = len(s), 0

for i in range(sLen):
    for till1 in range(i + 1, sLen + 1):
        till2 = till1 + 1
        for j in range(i + 1, sLen):
            if till2 > sLen:
                break
            sub1 = s[i:till1]
            sub2 = s[j:till2]
            subLen = len(sub1)
            if sub1 == sub2 and ans < subLen:
                ans = subLen
            till2 += 1

print(ans)