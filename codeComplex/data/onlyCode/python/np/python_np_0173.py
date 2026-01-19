def func():
    count = 0
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if 1 << j & i:
                temp.append(c[j])

        if l <= sum(temp) <= r and temp[-1] - temp[0] >= x:
            count += 1
    print(count)


n, l, r, x = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
func()
