def main():
    t = int(input())
    for i in range(t):
        n, k = input().split(' ')
        n = int(n)
        k = int(k)
        if n > 35:
            m = n - 1
            print('YES ' + m.__str__())
            continue
        if k > (4 ** n - 1) // 3:
            print('NO')
            continue
        ans = None
        for a in range(n):
            can = (2 ** (n - a + 1) - 1) * (4 ** a - 1) // 3
            total = (4 ** n - 1) // 3
            min = 2 ** (n - a + 1) - 2 - n + a
            if k <= total - can and k >= min:
                ans = a
                break
        if ans is not None:
            print("YES " + ans.__str__())
        else:
            print('NO')

if __name__ == "__main__":
    main()