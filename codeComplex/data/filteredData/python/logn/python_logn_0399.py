def main(n):
    ans = []
    mult = 1
    while n > 3:
        ans += [mult] * (n - n // 2)
        n //= 2
        mult *= 2
    if n == 3:
        ans += [mult, mult, mult * 3]
    elif n == 2:
        ans += [mult, mult * 2]

    else:
        ans += [mult]
    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)