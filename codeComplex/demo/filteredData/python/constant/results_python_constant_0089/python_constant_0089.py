def main(n):
    if n < 3:
        # print(n)
        pass
        return
    if n % 2 == 1:
        # print(n * (n - 1) * (n - 2))
        pass

    else:
        if n % 3 == 0:
            g = n - 2

        else:
            g = n
        # print((n - 1) * (n - 3) * g)
        pass
if __name__ == "__main__":
    main(10)