import sys
input=sys.stdin.readline
al=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
n=int(input())
s=[input().rstrip() for i in range(3)]
l=len(s[0])
ans=[0]*3
for c in al:
    for i in range(3):
        cnt_c=s[i].count(c)
        if cnt_c+n<=l:
            ans[i]=max(ans[i],cnt_c+n)
        else:
            if n==1 and l==cnt_c:
                ans[i]=max(ans[i],l-1)
            else:
                ans[i]=l
if (ans[0]==ans[1] and max(ans)==ans[0]) or (ans[1]==ans[2] and max(ans)==ans[1]) or (ans[0]==ans[2] and max(ans)==ans[2]):
    print("Draw")
elif max(ans)==ans[0]:
    print("Kuro")
elif max(ans)==ans[1]:
    print("Shiro")
else:
    print("Katie")