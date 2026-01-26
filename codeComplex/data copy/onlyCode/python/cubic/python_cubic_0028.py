string = input()
totalmax = 0;
for x in range(len(string)):
    curr = ""
    for y in string[x:]:
        curr +=y;
        if string[x:].rfind(curr) != string[x:].find(curr):
            totalmax = max(totalmax, len(curr))
            continue
print(totalmax)