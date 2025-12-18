n, m, k = map(int, input().split())
arr = [int(x) for x in input().split()]
modulo = 0
tmp = 0
op = 1
cur = (arr[0] - 1) // k
for i in range(m):
    if (arr[i] - 1 - modulo) // k != cur:
        modulo += tmp
        cur = (arr[i] - 1 - modulo) // k
        tmp = 0
        op += 1
    tmp += 1
print(op)