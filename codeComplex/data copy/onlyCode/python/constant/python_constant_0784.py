def checksq(n):
    m = int(n**0.5)
    if m * m == n:
        return m
    m += 1
    if m * m == n:
        return m
    return -1

def main():
    # n, m = map(int, input().split())
    n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    if n % 2 == 1:
        print("NO")
        return
    if checksq(n // 2) != -1:
        print('YES')
        return
    n //= 2
    if n % 2 == 1:
        print('NO')
        return
    if checksq(n // 2) != -1:
        print('YES')
    else:
        print('NO')




# for i in range(1):
for i in range(int(input())):
    main()