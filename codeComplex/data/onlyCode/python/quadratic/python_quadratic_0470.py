n = int(input())

L = list(map(int, input().split(" ")))
R = list(map(int, input().split(" ")))

LR = list(zip(L,R))

index_to_candies = {}
candy = n

for nn in range(n,0,-1):
    if(len(index_to_candies) == n):
        break

    #print(index_to_candies)
    #print(LR)

    zero_index = []
    for idx, (l,r) in enumerate(LR):
        if (l,r) == (0,0) and not idx in index_to_candies:
            index_to_candies[idx] = nn
            zero_index.append(idx)

    if len(zero_index) == 0:
        print("NO")
        exit()

    dec_left = 0
    dec_right = len(zero_index)
    zero_index_idx = 0

    for idx, (l,r) in enumerate(LR):
        if zero_index_idx < len(zero_index) and zero_index[zero_index_idx] == idx:
    #        print(idx)
            zero_index_idx += 1
            dec_left += 1
            dec_right -= 1

        if (l,r) != (0,0):
            LR[idx] = (l-dec_left,r-dec_right)
            if LR[idx][0] < 0 or LR[idx][1] < 0:
                print("NO")
                exit()
print("YES")
j = []
for i in range(n):
    j.append(str(index_to_candies[i]))
print(" ".join(j))
