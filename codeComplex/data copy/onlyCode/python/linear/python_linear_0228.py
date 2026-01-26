#time - O(n)
# space- O(1)

x=int(input())
s=input()

def substring(x,s):
    count=0
    ans=0
    
    for i in range(x):
        if s[i]=="x":
            count+=1
        else:
            if count>=3:
                ans+=count-2
            count=0
    if count>=3:
        ans+=count-2
    
    return ans
print(substring(x,s))