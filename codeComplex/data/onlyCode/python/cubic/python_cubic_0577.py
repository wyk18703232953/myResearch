def main():
    import sys
    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    a = list(str(a))
    a.sort()
    ans = []
    while a:
        for i in range(len(a) - 1, -1, -1):
            c = ans + [a[i]] + a[:i] + a[i+1:]
            if int(''.join(c)) <= b:
                ans.append(a[i])
                a.pop(i)
                break
    print(''.join(ans))


main()