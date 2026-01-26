def check(num):
    l = list(str(num))
    l = list(dict.fromkeys(l))
    if l==['4', '7'] or l==['7', '4'] or l==['4'] or l==['7']: return True
    else: return False

lucky = False
n = int(input())
for i in range(3, n+1):
    if n%i==0 and check(i): lucky=True
print("YES" if lucky else "NO")