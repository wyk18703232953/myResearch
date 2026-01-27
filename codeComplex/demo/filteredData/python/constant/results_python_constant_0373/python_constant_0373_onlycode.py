A, B, C, N = map(int, input().strip().split())
D = N - (A + B - C)
if D <= 0 or C > A or C > B:
    print('-1')
    exit(0)
print(D)
