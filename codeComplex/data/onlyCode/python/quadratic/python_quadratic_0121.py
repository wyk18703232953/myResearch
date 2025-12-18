n, m = list(map(int, input().split()))
square = [0] * n
l = list(map(int, input().split()))
for x in l:
    square[x-1] += 1
print(min(square))
    
