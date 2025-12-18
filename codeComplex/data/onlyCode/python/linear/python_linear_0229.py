# Time - O(n)
# Space - O(1)

n = int(input())
s = input()
count = 0
temp_count = 0
for c in s:
    if c == 'x':
        temp_count += 1
    else:
        temp_count = 0
    if temp_count == 3:
        count += 1
        temp_count -= 1

print(count)
