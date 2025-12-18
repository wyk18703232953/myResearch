a, b  = map(int, input().split())

k = 2**(a^b).bit_length()
print(k-1)