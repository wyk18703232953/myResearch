def main(n):
    n = n + 1
    result = 0 if not (n - 1) else n // 2 if not n & 1 else n
    # print(result)
    pass
if __name__ == "__main__":
    main(10)