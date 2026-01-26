import sys
n,m=map(int,input().split())
for i in range(n//2):
    for j in range(m):
        sys.stdout.write('{} {}\n'.format(*[i+1,j+1]))
        sys.stdout.write('{} {}\n'.format(*[n-i,m-j]))
if n%2:
    for j in range(m//2):
        sys.stdout.write('{} {}\n'.format(*[n//2+1,j+1]))
        sys.stdout.write('{} {}\n'.format(*[n//2+1,m-j]))
    if m%2:
        sys.stdout.write('{} {}\n'.format(*[n//2+1,m//2+1]))