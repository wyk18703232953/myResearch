n = int(input())
arr = set(map(int,input().split()))

def solve():
    for i in arr:
        for k in range(31):
            if i - (1 << k) in arr and i + (1 << k) in arr:
                return [i - (1 << k), i, i + (1 << k)]
    for i in arr:
        for k in range(31):
            if i + (1 << k) in arr:
                return [i, i + (1 << k)]
    
    for i in arr:
        return [i]

lst = solve()
# print(lst)
print(len(lst))
print(*lst)
