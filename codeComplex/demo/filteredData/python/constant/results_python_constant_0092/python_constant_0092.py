import math

def check(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n & 1:
        return (n - 1) * (n - 2) * n
    if math.gcd(n, n - 3) == 1:
        return n * (n - 1) * (n - 3)

    else:
        return (n - 1) * (n - 2) * (n - 3)

def main(n):
    # n is the input size; here we just use it directly as the original program did
    value = n
    result = check(value)
    # print(result)
    pass
if __name__ == "__main__":
    # example deterministic call; adjust n for larger/smaller input scale
    main(10)