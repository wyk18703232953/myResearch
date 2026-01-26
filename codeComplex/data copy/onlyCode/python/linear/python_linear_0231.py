a = int(input())
b = input()
s = 0
for i in range(a-2):
    if b[i:i+3] == 'xxx':
        s = s + 1
print(s)