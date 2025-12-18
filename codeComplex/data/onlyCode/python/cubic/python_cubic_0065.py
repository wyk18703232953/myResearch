# http://codeforces.com/contest/23/problem/A

string = input()
size = len(string)

ans_got = 0
for s in range(1,size)[::-1]:
    dic = {}
    for i in range(0,size-s+1):
        if(string[i:i+s] in dic):
            print(s)
            ans_got = 1
            break
        else:
            dic[string[i:i+s]] = 1
    if(ans_got == 1):
        break
if(ans_got == 0):
    print(0)