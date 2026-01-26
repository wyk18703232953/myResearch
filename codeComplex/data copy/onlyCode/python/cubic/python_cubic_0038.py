s = input()
pb = 0
lenght = len(s)-1
w = []
while(lenght!=0):
    ss = s[pb:pb+lenght]
    w.append(ss)
    if pb+lenght==len(s):
        pb = 0
        lenght -= 1
    else:
        pb+=1
for i in range(0,len(w)-1):
    for j in range(i+1,len(w)):
        if (w[i]==w[j]):
            print(len(w[i]))
            exit(0)
print(0)

    
