n = int(input())

nums = list(map(int, input().split()))
costs = list(map(int, input().split()))


k = -1

for i in range(n):
    
    kc = -1
    for c in range(i + 1, n):
        if nums[i] < nums[c] and (kc == -1 or kc > costs[c]):
            if kc == -1:
                kc = costs[c]
            kc = costs[c]
     
    if kc > -1:
        nat = kc
        kc = -1
        for c in range(i):
            if nums[i] > nums[c] and (kc == -1 or kc > costs[c]):
                if kc == -1:
                    kc = costs[c]
              
                kc = costs[c]
        
        if kc > -1:
            if k == -1:
                k = nat + kc + costs[i]
            k = min(nat + kc + costs[i], k)

print(k)    

    
    
    
