def chk(n):
    return int(n**0.5+0.1)**2 == n
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0 and chk(n//2) or n % 4 == 0 and chk(n//4):
        print("YES")
    else:
        print("NO")
