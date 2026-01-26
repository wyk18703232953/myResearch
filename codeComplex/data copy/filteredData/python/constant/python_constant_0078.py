def main(n):
    if n < 3:
        # print(n)
        pass

    else:
        if n % 2 != 0:
            # print(n * (n - 1) * (n - 2))
            pass
        elif n % 3 == 0:
            # print((n - 1) * (n - 2) * (n - 3))
            pass

        else:
            # print(n * (n - 1) * (n - 3))
            pass
if __name__ == "__main__":
    main(10)