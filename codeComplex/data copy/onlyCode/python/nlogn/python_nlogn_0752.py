def solve(n, a):
    a = sorted(a)
    if n == 1:
        return a[0] > 0 and a[0] % 2 == 1
    same_count = 0
    for i in range(n - 1):
        if a[i] == a[i + 1] == 0:
            return False
        if i < n - 2 and a[i] + 1 == a[i + 1] == a[i + 2]:
            return False
        if a[i] == a[i + 1]:
            same_count += 1
    if same_count > 1:
        return False
    return (sum(a) - n * (n - 1) // 2) % 2 == 1



assert not solve(1, [0])
assert not solve(2, [1, 0])
assert solve(2, [2, 2])
assert solve(3, [2, 3, 1])
assert not solve(4, [1, 1, 2, 2])
assert solve(4, [1, 1, 2, 3])
assert not solve(4, [1, 2, 3, 4])
assert solve(4, [0, 1, 2, 4])
assert solve(5, [0, 1, 2, 3, 5])

n = int(input())
a = map(int, input().split())

r = solve(n, a)
if r:

    print('sjfnb')
else:
    print('cslnb')
