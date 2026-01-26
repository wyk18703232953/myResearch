N = int(input())
src = [tuple(map(int,input().split() + [i])) for i in range(N)]
src.sort()

prev_l = max_r = 0
prev_i = outer = -1
for l,r,i in src:
    if prev_l == l:
        print(prev_i+1, i+1)
        exit()
    if r <= max_r:
        print(i+1, outer+1)
        exit()
    else:
        max_r = r
        outer = i
    prev_l = l
    prev_i = i
print(-1,-1)
