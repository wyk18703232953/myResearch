
n = input()

m = 0
for i in range(len(n)):

    for j in range(i,len(n)+1):

        if len(n[i:j])>m and n[i:j] in n[i+1:len(n)]:

            m = len(n[i:j])

print(m)
