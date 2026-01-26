n, m = (int(x) for x in input().split())
boys_out = sorted([int(x) for x in input().split()], reverse=True)
girls_in = sorted([int(x) for x in input().split()])
max_boy = max(boys_out)
ans = 0
for boy in boys_out:
    ans += boy * m

count = 0
i = 0
for girl in girls_in:
    if girl < max_boy:
        print(-1)
        quit()
        
    if girl > max_boy:
        if count == m - 1:
            count = 0
            i += 1
        if i >= n:
            print(-1)
            quit()
        ans += girl - boys_out[i]
        count += 1

print(ans)              