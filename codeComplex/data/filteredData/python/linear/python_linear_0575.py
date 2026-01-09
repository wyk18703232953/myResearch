def solve(n, k):
    # print(1 * k, end=' ')
    pass

    if n == 2:
        # print(2 * k, end=' ')
        pass
    if n == 3:
        # print(k, 3 * k, end=' ')
        pass

    else:
        temp = n // 2
        if n % 2 == 0:
            temp -= 1
        # print((str(k) + ' ') * temp, end='')
        pass

        if n > 3:
            solve(n // 2, k * 2)

def main(n):
    solve(n, 1)

if __name__ == "__main__":
    main(10)