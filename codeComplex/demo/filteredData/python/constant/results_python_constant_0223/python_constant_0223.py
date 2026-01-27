def main(n):
    # n controls the magnitude of generated integers
    a = n
    b = 2 * n
    x = 3 * n
    y = 4 * n
    z = 5 * n
    result = max((0, 2 * x + y - a)) + max((0, 3 * z + y - b))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)