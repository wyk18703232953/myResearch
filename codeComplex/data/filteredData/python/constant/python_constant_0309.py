import math

def main(n):
    # Interpret n as the value for the original variable n,
    # and deterministically derive k, s, p from it.
    # Ensure no division by zero.
    k = n + 1
    s = n // 2 + 1
    p = (n % 5) + 1

    sheets = math.ceil(n / s) * k
    result = math.ceil(sheets / p)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)