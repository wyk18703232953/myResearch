a,b=map(int,input().split())
print((1<<(a^b).bit_length())-1)