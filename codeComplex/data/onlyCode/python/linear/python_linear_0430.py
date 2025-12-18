n = int(input())
r = 1
t = sum(map(int, input().split()))
for i in range(n - 1):
    if sum(map(int, input().split())) > t:
        r += 1

print(r)