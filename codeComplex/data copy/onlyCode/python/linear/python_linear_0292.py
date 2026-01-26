# A. Nastya and an Array

n = int(input())
a = set(map(int, input().split()))

ans = len(a) - 1 if 0 in a else len(a)
print(ans)
