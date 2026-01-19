import math
xy = list(map(int,input().split()))
x = [[xy[0],xy[2],xy[4]],[xy[1],xy[3],xy[5]]]
aa = 0
max_ll = 0
for i in range(3):
    aa += x[0][i]*x[1][i]
    max_ll = max(max_ll,x[0][i],x[1][i])

bb = math.sqrt(aa)
# print(bb)
if bb*bb!=aa or max_ll!=bb:
    print(-1)
else:
    bb = int(bb)
    mt = [['']*bb for _ in range(bb)]
    max_l = 0
    chars = ['A','B','C']
    x = [[xy[0],xy[1]],[xy[2],xy[3]],[xy[4],xy[5]]]
    max_lp = -1
    max_li = -1
    ii=0
    oh = []
    for i in x:
        if max(i)>=max_l:
            max_l = max(i)
            max_lp = sum(i)-max(i)
            max_li = ii
        # else:
        #     oh+=[ii]
        ii+=1
    
    max_ls = []
    ii=0
    for i in x:
        if max(i)==max_l:
            max_ls.append(i+[ii])
        else:
            oh+=[ii]
        ii+=1
    if len(max_ls)==3:
        # print('hey')
        # print(max_ls)
        for i in range(max_l):
            for j in range(max_l):
                if i<(max_ls[0][0]+max_ls[0][1]-max_l):
                    mt[i][j] = chars[max_ls[0][2]]
                elif i<(max_ls[0][0]+max_ls[0][1]-max_l + max_ls[1][0]+max_ls[1][1]-max_l):
                    mt[i][j] = chars[max_ls[1][2]]
                else:
                    mt[i][j] = chars[max_ls[2][2]]
    else:
        # print(oh)
        for i in range(max_lp):
            for j in range(max_l):
                mt[i][j] = chars[max_li]
        
        bb = max_l-max_lp
        for i in range(max_lp,max_l):
            for j in range(max_l):
                if j<(sum(x[oh[0]])-bb):
                    mt[i][j] = chars[oh[0]]
                else:
                    mt[i][j] = chars[oh[1]]
    
    print(max_l)
    for j in mt:
        print(''.join(j))
    # print(mt)


# for i in [0,1]:
#     for j in [0,1]:
#         for k in [0,1]:
#             a = x[i][0]+x[j][1]+x[k][2]
#             b = x[1-i][0]+x[1-j][1]+x[1-k][2]
#             if a==b:
