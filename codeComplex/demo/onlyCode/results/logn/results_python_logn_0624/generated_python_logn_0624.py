def main(n):
    k = n // 2
    return int((2 * n + 3 - (8 * n + 8 * k + 9) ** 0.5) // 2)

if __name__ == "__main__":
    print(main(10))