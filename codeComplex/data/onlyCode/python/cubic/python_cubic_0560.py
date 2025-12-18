a = input()
b = input()
list_a = list(a)
list_a.sort()
max_a = int(''.join(list_a))
for i in range(len(a)):
    for j in range(i+1, len(a)):
        list_a[i], list_a[j] = list_a[j], list_a[i]
        temp_a = int(''.join(list_a))
        if int(b) < temp_a or temp_a <= max_a:
            list_a[i], list_a[j] = list_a[j], list_a[i]
        else:
            max_a = temp_a
print(max_a)