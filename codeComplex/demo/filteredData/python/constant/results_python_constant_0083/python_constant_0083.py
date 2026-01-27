def main(n):
    if n <= 0:
        return
    if n == 1 or n == 2:
        # print(n)
        pass
    elif n % 2 != 0:
        m = n * (n - 1) * (n - 2)
        # print(m)
        pass
    elif n % 3 != 0:
        m = n * (n - 1) * (n - 3)
        # print(m)
        pass

    else:
        m = (n - 1) * (n - 2) * (n - 3)
        # print(m)
        pass
if __name__ == "__main__":
    main(10)