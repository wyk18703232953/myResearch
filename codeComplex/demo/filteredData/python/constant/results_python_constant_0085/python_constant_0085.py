def main(n):
    ans = 0
    if n == 1:
        # print(1)
        pass
        return
    if n == 2:
        # print(2)
        pass
        return
    if n == 3:
        # print(6)
        pass
        return
    if n % 2 == 0:
        if n % 3 == 0:
            ans = (n - 1) * (n - 2) * (n - 3)

        else:
            ans = n * (n - 1) * (n - 3)

    else:
        ans = n * (n - 1) * (n - 2)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)