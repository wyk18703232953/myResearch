n, l, r, x = map(int, input().split())
tasks = [int(i) for i in input().split()]
cnt = 0
for num in range(2 ** n):
    bin_num = bin(num)[2:]
    if len(bin_num) < n:
        bin_num = '0' * (n - len(bin_num)) + bin_num
    m = []
    for i in range(n):
        if bin_num[i] == '1':
            m.append(tasks[i])
    if sum(m) >= l and sum(m) <= r and max(m) - min(m) >= x:
        cnt += 1
print(cnt)