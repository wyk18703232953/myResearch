'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
n,kk=map(int,input().split())
s=input()
if(s==s[::-1] or s!=s[::-1]):
    k=""
    l=0
    for i in reversed(range(1,n)):
        k=s[i]+k
        #print(k)
        if(s.startswith(k)):
            l=len(k)
    ss=s[l:]
    fs=s+(ss*(kk-1))
    print(fs)
        
