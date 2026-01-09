import math

def solve(n):
    if not n % 2 and math.sqrt(n // 2) == int(math.sqrt(n // 2)):
        # print('YES')
        pass
        return
    if not n % 4 and math.sqrt(n // 4) == int(math.sqrt(n // 4)):
        # print('YES')
        pass
        return
    # print('NO')
    pass

def main(n):
    t = n
    for i in range(1, t + 1):
        solve(i)

if __name__ == "__main__":
    main(10)