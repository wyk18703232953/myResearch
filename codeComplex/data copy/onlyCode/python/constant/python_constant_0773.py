read = lambda: map(int, input().split())
def sq(x):
    return int(x ** 0.5) ** 2 == x
t = int(input())
for _ in range(t):
    n = int(input())
    if (n % 2 == 0 and sq(n // 2)) or (n % 4 == 0 and sq(n // 4)):
        print('YES')
    else:
        print('NO')