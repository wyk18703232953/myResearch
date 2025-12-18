x = int(input())
list1 = []
for i in range(x):
    value = input()
    list1.append(value)

for i in range(x):
    value = input()
    if value in list1:
        list1.remove(value)

print(len(list1))

