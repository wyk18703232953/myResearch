def main(n):
    a = n
    b = n // 2
    k = 2**(a ^ b).bit_length() - 1
    # print(k)
    pass
if __name__ == "__main__":
    main(10)