a,b = map(int,input().split())
a,b = min(a, b), max(a, b)
A = bin(a)[2:]
B = bin(b)[2:]
A = "0" * (len(B) - len(A)) + A
diff = 0
for i in range(len(A)):
    if(A[i]!=B[i]):
        diff = len(A) - i
        break
print((2**diff) - 1)
