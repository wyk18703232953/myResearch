x=input()
a=0
for i in range(len(x)):
    for j in range(i,len(x)):
        if x[i:j] in x[i+1:]:
            if len(x[i:j])>a:
                a=len(x[i:j])
print(a)
