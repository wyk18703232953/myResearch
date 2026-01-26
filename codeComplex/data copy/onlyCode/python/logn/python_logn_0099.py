def main():
    a, b = map(int, input().split())
    K = 60
    if a == b:
        ans = 0
    else:
        curr = K
        while (b & (1 << curr)) == (a & (1 << curr)):
            curr -= 1
        ans = (1 << curr)
        curr -= 1
        lb = False
        ga = False
        for i in range(curr, -1, -1):
            if (b & (1 << i)) == 0 and (a & (1 << i)) == 0:
                if not lb:
                    ans += (1 << i)
                    ga = True
                else:
                    ans += (1 << i)
            elif (b & (1 << i)) == 0 and (a & (1 << i)) == 1:
                ans += (1 << i)
            elif (b & (1 << i)) == 1 and (a & (1 << i)) == 0:
                if not lb:
                    ans += (1 << i)
                    ga = True
                    lb = True
                else:
                    ans += (1 << i)
            else:
                if not lb:
                    ans += (1 << i)
                    lb = True
                else:
                    ans += (1 << i)
    print(ans)


if __name__ == '__main__':
    main()