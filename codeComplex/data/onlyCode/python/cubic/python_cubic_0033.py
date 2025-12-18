s = input()
res = 0
solve = 0
for pos in range(1,len(s)):
    for i in range(len(s) - pos):
        if s[i:i+pos] in s[i+1:]:
            if solve < pos:
                solve = pos
print(solve)