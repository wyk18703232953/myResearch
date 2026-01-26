import sys
from collections import Counter

input = sys.stdin.readline
testcase=int(sys.stdin.readline())
A=[list(map(int,input().split())) for i in range(testcase*2)]

for t in range(testcase):
    counter=Counter(A[t*2+1])
    LIST=[]
    for c in counter:
        if counter[c]>=4:
            print(c,c,c,c)
            break
        elif counter[c]>=2:
            LIST.append(c)
    else:
        LIST.sort()
        #print(LIST)
        ANS=[LIST[0],LIST[1],LIST[1]/LIST[0]]
        for i in range(2,len(LIST)):
            if LIST[i]/LIST[i-1]<ANS[2]:
                ANS=[LIST[i-1],LIST[i],LIST[i]/LIST[i-1]]

        print(ANS[0],ANS[0],ANS[1],ANS[1])
            


