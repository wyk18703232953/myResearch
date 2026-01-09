def main(n):
    # Deterministically generate a, b, c based on n
    a = n // 2
    b = n // 3
    c = n // 4

    result = n - a - b + c
    output = result if result > 0 and c <= a and c <= b else -1
    # print(output)
    pass
if __name__ == "__main__":
    main(1000)