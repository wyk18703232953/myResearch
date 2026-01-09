def main(n):
    # n controls the length of the string s
    # Deterministically generate s of length n using a simple pattern
    s = ''.join('-' if i % 2 == 0 else '+' for i in range(n))

    ans = 10000
    for i in range(0, 105):
        f = True
        x = i
        for c in s:
            if c == '-':
                x -= 1

            else:
                x += 1
            if x < 0:
                f = False
        if f:
            ans = min(ans, x)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)