n = int(input())
a = list(map(int, input().split()))
d = set(a)
if (0 in a): 
    print(len(d)-1)
else:
    print(len(d))