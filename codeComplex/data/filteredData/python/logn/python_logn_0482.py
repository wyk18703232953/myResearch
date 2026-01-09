import math

def main(n):
    k = 1
    temp_n = n
    while temp_n > 9 * k * (10 ** (k - 1)):
        temp_n = temp_n - 9 * k * (10 ** (k - 1))
        k = k + 1
    remainder = temp_n % k
    if remainder == 0:
        remainder = k
    if k == 1:
        quoteint = math.ceil(temp_n / k)

    else:
        adder = "9" * (k - 1)
        adder = int(adder)
        quoteint = math.ceil(temp_n / k) + adder
    # print(str(quoteint)[remainder - 1])
    pass
if __name__ == "__main__":
    main(10)