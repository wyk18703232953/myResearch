def main(n):
    # Interpret n as scaling factor for all inputs
    a = 2 * n
    b = 3 * n
    x = n
    y = 2 * n
    z = 3 * n

    needa = 2 * x + y
    needb = y + 3 * z
    result = max(0, needa - a) + max(0, needb - b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)