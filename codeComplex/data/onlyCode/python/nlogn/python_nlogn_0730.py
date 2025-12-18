a = (input().split())
a.sort()
#print(a)
if(a[0] == a[1] == a[2]):
    print(0)
    exit()
elif(a[0] == a[1] or a[1] == a[2]):
    print(1)
    exit()
    
a1 = []
for i in range(3):
    a1.append([int(a[i][0]), a[i][1]])
a1.sort()
#print(a1)
if(a1[1][1] == a1[2][1] == a1[0][1]):
    if(a1[0][0] == a1[1][0] - 1 and a1[0][0] == a1[2][0] - 2):
        print(0)
        exit()
    found = False
    for i in range(3):
        for j in range(3):
            if(abs(a1[i][0] - a1[j][0]) == 1 or abs(a1[i][0] - a1[j][0]) == 2 ):
                print(1)
                exit()
    print(2)
    exit()
for i in range(3):
    for j in range(i + 1, 3):
        if(a1[i][1] == a1[j][1]):
            if(a1[i][0] == a1[j][0] - 1 or a1[i][0] == a1[j][0] - 2):
                print(1)
            else:
                print(2)
            exit()
print(2)

            


