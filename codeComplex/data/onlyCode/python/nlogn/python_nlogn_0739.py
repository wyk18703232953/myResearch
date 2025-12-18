from sys import stdin, stdout, exit

n = int(input())
a = list(map(int, stdin.readline().split()))

def z(winner):
    return 'sjfnb' if winner == 0 else 'cslnb'

a.sort()
dups = set(a)
if len(dups) < len(a) - 1:
    print(z(1))
    exit()

winner = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        if a[i] == 0 or a[i]-1 in a:
            print(z(1))
            exit()
        winner = 1
        a[i] = a[i] - 1

s = sum(a)
final = n*(n-1) // 2
winner += (s - final) + 1
winner %= 2
print(z(winner))
