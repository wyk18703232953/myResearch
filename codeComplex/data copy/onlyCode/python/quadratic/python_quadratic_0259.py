
from collections import defaultdict

n,a,b = map(int,input().split())

hash = defaultdict(list)

# debug
# def dfs(n):
# 
# 
#     bool[n] = True
#     for i in hash[n]:
#         if bool[i] == False:
#             dfs(i)



if a == 1 and b == 1:
    if n == 2 or n == 3:
        print('NO')
        exit()

if a == 1 or b == 1:


    bool = [False]*(n+1)

    if a>n or b>n:
        print('NO')
        exit()
    print('YES')

    l = []
    for i in range(n):
        z = ['0']*(n)
        l.append(z)
    ans = []

    for i in range(n):
        z = ['0']*(n)
        ans.append(z)

    if b == 1:




        for i in range(a-1,n-1):
            # hash[i].add(i+1)
            # hash[i+1].add(i)
            l[i][i+1] = '1'
            l[i+1][i] = '1'
            # hash[i+1].append(i)
            # hash[i].append(i+1)


        # count = 0
        # for i in range(n):
        #     if bool[i] == False:
        #
        #         dfs(i)
        #         count+=1
        # if a == 1 and b == 1:

        for i in l:
            print(''.join(i))
    else:


        ans = []

        for i in range(n):
           z = ['0']*(n)
           ans.append(z)

        for i in range(b-1,n-1):
            # hash[i].add(i+1)
            # hash[i+1].add(i)
            l[i][i+1] = '1'
            l[i+1][i] = '1'
            # hash[i+1].append(i)
            # hash[i].append(i+1)
        # for i in l:
        #     print(*i)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if l[i][j] == '1':
                        ans[i][j] = '0'
                    if l[i][j] == '0':
                        ans[i][j] = '1'
                        # hash[i+1].append(j+1)
        # count = 0
        # for i in range(n):
        #     if bool[i] == False:
        #
        #         dfs(i)
        #         count+=1


        for i in ans:
            print(''.join(i))



else:
    print('NO')

