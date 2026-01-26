import math

def main(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        x = math.floor(n / 2 + 1) * math.floor(n / 2)

    else:
        x = math.ceil(n / 2) * math.ceil(n / 2)
    # print(x)
    pass
    return x

if __name__ == "__main__":
    main(10)