n = int(input())
if n <= 5:
    print(-1)
    for i in range(2, n+1):
        print(1, i)
    exit()

print(1, 2)
print(2, 3)
print(2, 4)
for i in range(5, n+1):
    print(3, i)

for i in range(2, n+1):
    print(1, i)
