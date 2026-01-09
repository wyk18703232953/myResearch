def main(n):
    if n > -1:
        # print(n)
        pass

    else:
        s = str(n)
        x = int(s[:len(s) - 1])
        y = int(s[:len(s) - 2] + s[-1])
        # print(max(x, y))
        pass
if __name__ == "__main__":
    main(123)
    main(-123)
    main(0)