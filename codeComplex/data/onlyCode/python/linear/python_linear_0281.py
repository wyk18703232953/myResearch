from sys import stdin
n, m, a, b = map(int, stdin.readline().split())
x = n%m
print(min(a *(m-x), b*x))