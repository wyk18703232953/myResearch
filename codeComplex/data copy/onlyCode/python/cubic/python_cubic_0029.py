line = input()
n = len(line)
temp = [0]
for i in range(1, n):
    for j in range(n-i):
        for k in range(1, n-i-j+1):
            # print(line[j:j+i+1])
            # print(line[j+k:j+k+i+1])
            if line[j:j+i] == line[j+k:j+k+i]:
                temp.append(i)
print(max(temp))