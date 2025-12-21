def main(n):
    if n == 0:
        return 0, 0, 0
    a, b = 0, 1
    while a + b != n:
        a, b = b, a + b
    return 0, a, b

if __name__ == "__main__":
    print(main(10))