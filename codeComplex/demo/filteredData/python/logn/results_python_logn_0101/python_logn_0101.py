def main(n):
    a = n
    b = 2 * n + 1
    a = a ^ b
    k = 0
    while a:
        k += 1
        a = a >> 1
    result = 2 ** k - 1
    return result

if __name__ == "__main__":
    # print(main(10))
    pass