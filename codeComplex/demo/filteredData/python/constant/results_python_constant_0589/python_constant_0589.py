def main(n):
    # n represents q (the size of the input)
    q = n
    # Deterministically generate a and s based on n
    a = n // 2 + 1
    s = n // 3 + 2

    if (a + s - 2) <= (q + q - a - s):
        # print("White")
        pass

    else:
        # print("Black")
        pass
if __name__ == "__main__":
    main(10)