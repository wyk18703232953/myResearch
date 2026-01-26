string = input().strip()
mx = 0

for i in range(len(string)):
    for j in range(i+1, len(string)):
        m = 0
        while(j+m < len(string) and string[i+m] == string[j+m]):
            m += 1
        mx = max(mx, m)

print(mx)