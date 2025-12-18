nab = [int(i) for i in input().split()]
n = nab[0]
a = nab[1]
b = nab[2]
h = sorted([int(i) for i in input().split()])
print(h[b] - h[b-1])
