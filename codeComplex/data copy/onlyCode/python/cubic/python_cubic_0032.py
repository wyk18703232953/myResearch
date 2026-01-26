inputS=input()
ans=0

for i in range (0,len(inputS)-1):
    for count in range(1,len(inputS)):
        for j in range(i+1, len(inputS)-count+1):
            A=inputS[i: i+count]
            B=inputS[j: j+count]
            if A==B:
                ans=count if count>ans else ans

print(ans)