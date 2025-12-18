s=input()
length=len(s)
answer=[ ]
for i in range (0,length):
    for j in range(i+1,length+1):
        k=s[i:j]
        co=0
        for u in range (0,length):
            if(s[u:].startswith(k)):
                co+=1
        if(co>=2):
            #answer=max(answer,len(k))
            answer.append(len(k))
if(len(set(s))==length):
    print('0')
else:
    print(max(answer))

