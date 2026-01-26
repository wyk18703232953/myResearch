a, b = input().split()
li = []
for i in range(len(a)):
    li.append(a[:i + 1] + b[0])
li.sort()
print(li[0])
