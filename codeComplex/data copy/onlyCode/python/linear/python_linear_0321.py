n = int(input())
 
a = [input() for _ in range(n)]
b = [input() for _ in range(n)]
 
cost = 0
for s in ["M", "S", "XS", "XXS", "XXXS", "L", "XL", "XXL", "XXXL"]:
    ca = a.count(s)
    cb = b.count(s)
    cost += ca - min(ca, cb)
    
print(cost)