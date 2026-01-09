def main(n):
    a = n
    b = n + 1  # unused, kept to mirror original two-input structure
    q, r = divmod(a, 2)
    result = '01' * q + '0' * r
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)