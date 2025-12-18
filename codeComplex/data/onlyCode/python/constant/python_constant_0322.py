grid = list(map(int,input().split()))
max_res = 0
for i in range(14):
    g_c = grid.copy()
    Amount = g_c[i]//14
    Amount_r = g_c[i]%14
    if(Amount > 0):    
        for j in range(14):
            if i != (i+j+1)%14:
                g_c[(i+j+1)%14]+=Amount
                g_c[i]-=Amount    
    if Amount_r > 0:
        for j in range(14):
            if Amount_r > 0:
                if i != (i+j+1)%14:
                    g_c[(i+j+1)%14]+=1
                    Amount_r-=1
                    g_c[i]-=1
            else:
                break
    
    res = 0
    for i in range(14):
        if g_c[i] % 2 ==0:    
            res+=g_c[i]
      
    max_res = max(max_res,res)

print(max_res)  
    