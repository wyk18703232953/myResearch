def main(n):
    n = n - 1
    x = 1
    y = 9
    while n > x * y:
        n -= x * y
        y *= 10
        x += 1
    a = 10 ** (x - 1)
    a += n // x
    return str(a)[n % x]

if __name__ == "__main__":
    print(main(100))