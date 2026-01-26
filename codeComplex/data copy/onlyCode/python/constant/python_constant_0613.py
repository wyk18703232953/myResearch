input = raw_input

def f(n):
    t = (n + 1) // 2
    return t if n % 2 == 0 else -t

for i in range(int(input())):
    le, rg = map(int, input().split())

    print(f(rg) - f(le - 1))
