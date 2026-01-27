def main(n):
    l = list(str(n))
    if n >= 0:
        # print(n)
        pass

    else:
        if int(l[-1]) > int(l[-2]):
            l.pop(-1)

        else:
            l.pop(-2)
        # print(int(''.join(l)))
        pass
if __name__ == "__main__":
    main(123)
    main(-123)
    main(-100)
    main(0)