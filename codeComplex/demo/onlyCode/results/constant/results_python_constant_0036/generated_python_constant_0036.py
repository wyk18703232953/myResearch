def main(n):
    n = int(n)
    n = n + n // 2
    return n

if __name__ == "__main__":
    print(main(10))