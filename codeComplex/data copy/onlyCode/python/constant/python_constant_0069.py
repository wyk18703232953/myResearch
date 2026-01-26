
n = int(input())
fib = [0,1]

for x in range(1,200):


    z = fib[x] + fib[x-1]
    if z <= n:

        fib.append(z)
    else:
        break

fib = fib[::-1]
lis = []
for y in range(len(fib)):

    if fib[y] <= n:
        if (sum(lis) + fib[y]) <= n:
            if len(lis) < 3:
                lis.append(fib[y])
if sum(lis) == n:
    if len(lis) == 1:
        lis.append(0)
        lis.append(0)
        print(*lis)
    elif len(lis) == 2:
        lis.append(0)
        print(*lis)
    else:
        print(*lis)
else:
    print("I'm too stupid to solve this problem")


