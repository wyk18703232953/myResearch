n = int(input())

string = input()
i = 0
j = 0
total = 0

while j < len(string):
    bool = False
    count = 0
    while j < len(string) and string[i] == 'x' and string[j] == 'x':
        count += 1
        bool = True
        j += 1

    if count >= 3:
        total += (count-3)+1
    if bool:
        i = j
    else:
        i += 1
        j += 1



print(total)
